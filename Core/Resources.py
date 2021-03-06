import xml.dom.minidom, copy, random
from Core.AbstractGraph import AbstractGraph, AbstractVertex
from Core.Demands import DemandStorage, VM

class State:
    def __init__(self):
        self.demands = {}

class ComputerState(State):
    def __init__(self):
        State.__init__(self)
        self.usedSpeed = 0
        self.usedRam = 0

class StorageState(State):
    def __init__(self):
        State.__init__(self)
        self.usedVolume = 0

class RouterState(State):
    def __init__(self):
        State.__init__(self)
        self.usedCapacity = 0

class LinkState(State):
    def __init__(self):
        State.__init__(self)
        self.usedCapacity = 0

class Storage(AbstractVertex):
    ''' Storage element

    :param id: name
    :param volume: storage size
    :param type: storage type (enum/int)
    '''
    def __init__(self, id, volume, type):
        AbstractVertex.__init__(self, id)
        self.volume = volume
        self.type = type
        self.intervals = {}

    def getUsedVolumePercent(self, t):
        return 0 if self.volume == 0 or not t in self.intervals else self.intervals[t].usedVolume * 100.0 / self.volume

class Computer(AbstractVertex):
    ''' Computer element

    :param id: name
    :param speed: computer performance
    :param ram: RAM capacity
    '''
    def __init__(self, id, speed, ram):
        AbstractVertex.__init__(self, id)
        self.speed = speed
        self.ram = ram
        self.intervals = {}

    def getUsedSpeedPercent(self, t):
        return 0 if self.speed == 0 or not t in self.intervals else self.intervals[t].usedSpeed * 100.0 / self.speed

    def getUsedRamPercent(self, t):
        return 0 if self.ram == 0 or not t in self.intervals else self.intervals[t].usedRam * 100.0 / self.ram

class Router(AbstractVertex):
    ''' Router/switch element

    :param id: name
    :param capcity: total channel bandwidth
    '''
    def __init__(self, id, capacity):
        AbstractVertex.__init__(self, id)
        self.capacity = capacity
        self.intervals = {}

    def getUsedCapacityPercent(self, t):
        return 0 if self.capacity == 0 or not t in self.intervals else self.intervals[t].usedCapacity * 100.0 / self.capacity

class Link:
    ''' Channe;

    :param e1: first node
    :param e2: second node
    :param capacity: bandwidth
    '''
    def __init__(self, e1, e2, capacity):
        self.e1 = e1
        self.e2 = e2
        self.capacity = capacity
        self.intervals = {}

    def getUsedCapacityPercent(self,t):
        return 0 if self.capacity == 0 or not t in self.intervals else self.intervals[t].usedCapacity * 100.0 / self.capacity

class ResourceGraph(AbstractGraph):
    ''' Graph of physical resources
    '''
    assignedDemands = set([])

    def __init__(self):
        AbstractGraph.__init__(self)

    def ExportToXml(self):
        '''
        :returns: string with XML representation
        '''
        dom = xml.dom.minidom.Document()
        root = self.CreateXml(dom)
        dom.appendChild(root)
        return dom.toprettyxml()

    def CreateXml(self, dom):
        root = dom.createElement("resources")
        # TODO: take some meaningful interval
        try:
            r = [q for q in self.vertices[0].intervals.keys()][0]
        except:
            r = None
        if r:
            root.setAttribute("time", str(r[0]))
        for v in self.vertices:
            if isinstance(v, Computer):
                tag = dom.createElement("computer")
                tag.setAttribute("speed", str(v.speed))
                tag.setAttribute("ramcapacity", str(v.ram))
                tag.setAttribute("used", str(v.intervals[r].usedSpeed) if r != None else "0")
                tag.setAttribute("usedram", str(v.intervals[r].usedRam) if r != None else "0")
            elif isinstance(v, Storage):
                tag = dom.createElement("storage")
                tag.setAttribute("volume", str(v.volume))
                tag.setAttribute("used", str(v.intervals[r].usedVolume) if r != None else "0")
                tag.setAttribute("type", str(v.type))
            elif isinstance(v, Router):
                tag = dom.createElement("router")
                tag.setAttribute("capacity", str(v.capacity))
                tag.setAttribute("used", str(v.intervals[r].usedCapacity) if r != None else "0")
            if v.x:
                tag.setAttribute("x", str(v.x))
                tag.setAttribute("y", str(v.y))
            tag.setAttribute("number", str(v.number))
            tag.setAttribute("name", str(v.id))
            root.appendChild(tag)
        for v in self.edges:
            tag = dom.createElement("link")
            tag.setAttribute("from", str(v.e1.number))
            tag.setAttribute("to", str(v.e2.number))
            tag.setAttribute("capacity", str(v.capacity))
            tag.setAttribute("used", str(v.intervals[r].usedCapacity) if r != None else "0")
            root.appendChild(tag)
        return root

    def LoadFromXML(self, filename):
        ''' Load edges and vertices from XML
        
        .. warning:: Describe XML format here'''
        f = open(filename, "r")
        dom = xml.dom.minidom.parse(f)
        self.vertices = []
        self.edges = []
        for node in dom.childNodes:
            if node.tagName == "resources":
                self.LoadFromXmlNode(node)
        f.close()

    def LoadFromXmlNode(self, node):
        #Parse vertices
        for vertex in node.childNodes:
            if isinstance(vertex, xml.dom.minidom.Text):
                continue
            if vertex.nodeName == "link":
                continue
            name = vertex.getAttribute("name")
            number = int(vertex.getAttribute("number"))
            if vertex.nodeName == "computer":
                speed = int(vertex.getAttribute("speed"))
                ram = int(vertex.getAttribute("ramcapacity")) if vertex.hasAttribute("ramcapacity") else 0
                v = Computer(name, speed, ram)
            elif vertex.nodeName == "storage":
                volume = int(vertex.getAttribute("volume"))
                type = int(vertex.getAttribute("type"))
                v = Storage(name, volume, type)
            elif vertex.nodeName == "router":
                capacity = int(vertex.getAttribute("capacity"))
                v = Router(name,capacity)
            x = vertex.getAttribute("x")
            y = vertex.getAttribute("y")
            if x != '':
                v.x = float(x)
            if y != '':
                v.y = float(y)
            v.number = number
            self.vertices.append(v)

        self.vertices.sort(key=lambda x: x.number)
                    
        #Parse edges
        for edge in node.childNodes:
            if edge.nodeName == "link":
                source = int(edge.getAttribute("from"))
                destination = int(edge.getAttribute("to"))
                cap = int(edge.getAttribute("capacity"))
                e = Link(self.vertices[source-1], self.vertices[destination-1], cap)
                self.edges.append(e)

        self._buildPaths()

    def FindPath(self, v1, v2):
        if not self.PathExists(v1, v2):
            return
        comp = self.compdict[v1]
        paths = [[v1]]
        while True:
            newpaths = []
            for p in paths:
                last = p[len(p)-1]
                links = self.FindAllEdges(v1=last)
                for e in links:
                    other = e.e2 if e.e1 == last else e.e1
                    if v2 == other:
                        yield p + [e, v2]
                    if isinstance(other, Router):
                        if len(p)== 1 or ((len(p) >= 3) and (p[-3] != other) and (p.count(other) == 0)):
                            newpaths.append(p + [e, other])
            if newpaths == []:
                break
            paths = newpaths

    def GetTimeBounds(self):
        t1 = 0
        t0 = 0
        if not (self.vertices == []) and  not (self.vertices[0].intervals.keys() == []):
            t0 = self.vertices[0].intervals.keys()[0][0]
        for v in self.vertices:
            for t in v.intervals.keys():
                if t[1] > t1:
                    t1 = t[1]
                if t[0] < t0:
                    t0 = t[0]
        return (t0, t1)

    def GetTimeInterval(self, time):
        for v in self.vertices:
            for t in v.intervals.keys():
                if (time >= t[0]) and (time <= t[1]):
                    return t

    def GetAvailableVertices(self,v,time):
        availableVertices = set([])
        for v1 in self.vertices:
            if (isinstance(v, VM) and isinstance(v1, Computer)
                and (v.speed <= v1.speed - v1.intervals[time].usedResource) and (v.ram <= v1.ram - v1.intervals[time].usedRam)):
                availableVertices.add(v1)
            if isinstance(v, DemandStorage) and isinstance(v1, Storage) and (v.type == v1.type) and (v.volume <= v1.volume - v1.intervals[time].usedVolume):
                availableVertices.add(v1)
        return availableVertices

    def GetAvailableLinks(self, e, time):
        availableLinks = []
        g = self.FindPath(e.e1.resource, e.e2.resource)
        while True:
            try:
                p = g.next()
                if self.checkPath(p,e, time):
                    availableLinks.append(p)
            except StopIteration:
                return availableLinks

    def checkPath(self, path, link, time):
        for elem in path[1:len(path)-1]:
            if isinstance(elem, Router):
                if link.capacity > elem.capacity - elem.intervals[time].usedCapacity:
                    return False
            else:
                e = self.FindEdge(elem.e1, elem.e2)
                if link.capacity > e.capacity - e.intervals[time].usedCapacity:
                    return False
        return True

    def GetRanges(self, demand):
        v = self.vertices[0]
        ranges = []
        for t in v.intervals.keys():
            if (t[0] >= demand.startTime) and (t[1] <= demand.endTime):
                ranges.append(t)
        return ranges

    def DropVertex(self,demand,v):
        if v.resource == None:
            return
        for time in self.GetRanges(demand):
            if isinstance(v,VM):
                v.resource.intervals[time].usedSpeed -= v.speed
                v.resource.intervals[time].usedRam -= v.ram
            elif isinstance(v,DemandStorage):
                v.resource.intervals[time].usedVolume -= v.volume
            v.resource.intervals[time].demands[demand.id].remove(v.number)
            if v.resource.intervals[time].demands[demand.id]==[]:
                del v.resource.intervals[time].demands[demand.id]
        v.resource = None

    def DropLink(self,demand,link):
        if link.path == []:
            return
        path = link.path
        for elem in path[1:len(path)-1]:
            for time in self.GetRanges(demand):
                if isinstance(elem, Router):
                    elem.intervals[time].usedCapacity -= link.capacity
                    elem.intervals[time].demands[demand.id].remove((link.e1.number,link.e2.number))
                    if elem.intervals[time].demands[demand.id]==[]:
                        del elem.intervals[time].demands[demand.id]
                else:
                    e = self.FindEdge(elem.e1, elem.e2)
                    e.intervals[time].usedCapacity -= link.capacity
                    e.intervals[time].demands[demand.id].remove((link.e1.number,link.e2.number))
                    if e.intervals[time].demands[demand.id]==[]:
                        del e.intervals[time].demands[demand.id]
        link.path = []

    def DropDemand(self,demand):
        demand.assigned = False
        for r in demand.replications:
            self.DropReplica(demand,r)
        for rl in demand.replicalinks:
            self.DropReplicaLink(demand,rl)
        demand.replications = []
        demand.replicalinks = []
        for v in demand.vertices:
            self.DropVertex(demand,v)
        for e in demand.edges:
            self.DropLink(demand,e)
        if demand in self.assignedDemands:
            self.assignedDemands.remove(demand) 
        #self.RemoveIntervals(demand)

    def AssignVertex(self, demand, vdemand, vresource, time):
        vdemand.resource = vresource
        self.assignedDemands.add(demand)
        if not vresource.intervals[time].demands.has_key(demand.id):
            vresource.intervals[time].demands[demand.id] = []
        vresource.intervals[time].demands[demand.id].append(vdemand.number)
        if isinstance(vdemand, VM):
            vresource.intervals[time].usedSpeed += vdemand.speed
            vresource.intervals[time].usedRam += vdemand.ram
        elif isinstance(vdemand, DemandStorage):
            vresource.intervals[time].usedVolume += vdemand.volume

    def AssignReplica(self, demand, replica, time):
        replica.assignedto.intervals[time].usedVolume += replica.replica.volume

    def DropReplica(self, demand, replica):
        if replica.assignedto == None:
            return
        for time in self.GetRanges(demand):
            replica.assignedto.intervals[time].usedVolume -= replica.replica.volume

    def AssignReplicaLink(self, demand, link, path, time):
        for elem in path[1:len(path)-1]:
            if isinstance(elem, Router):
                elem.intervals[time].usedCapacity += link.capacity
            else:
                e = self.FindEdge(elem.e1, elem.e2)
                e.intervals[time].usedCapacity += link.capacity

    def DropReplicaLink(self,demand,link):
        if link.path == []:
            return
        path = link.path
        for elem in path[1:len(path)-1]:
            for time in self.GetRanges(demand):
                if isinstance(elem, Router):
                    elem.intervals[time].usedCapacity -= link.capacity
                else:
                    e = self.FindEdge(elem.e1, elem.e2)
                    e.intervals[time].usedCapacity -= link.capacity
        link.path = []

    def AssignLink(self, demand, link, path, time):
        link.path = path
        self.assignedDemands.add(demand)
        for elem in path[1:len(path)-1]:
            if isinstance(elem, Router):
                elem.intervals[time].usedCapacity += link.capacity
                if not elem.intervals[time].demands.has_key(demand.id):
                    elem.intervals[time].demands[demand.id] = []
                elem.intervals[time].demands[demand.id].append((link.e1.number, link.e2.number))
            else:
                e = self.FindEdge(elem.e1, elem.e2)
                e.intervals[time].usedCapacity += link.capacity
                if not e.intervals[time].demands.has_key(demand.id):
                    e.intervals[time].demands[demand.id] = []
                e.intervals[time].demands[demand.id].append((link.e1.number, link.e2.number))

    def AddTimePoint(self, r, point):
        points = []
        for k in r.intervals.keys():
            points.extend([k[0],k[1]])
        points = list(set(points))
        points.sort()        
        if points.count(point) != 0:
            return
        if point > max(points):
            if isinstance(r, Computer):
                r.intervals[(max(points),point)] = ComputerState()
            elif isinstance(r, Storage):
                r.intervals[(max(points),point)] = StorageState()
            elif isinstance(r, Router):
                r.intervals[(max(points),point)] = RouterState()
            elif isinstance(r, Link):
                r.intervals[(max(points),point)] = LinkState()
            return
        if point < min(points):
            if isinstance(r, Computer):
                r.intervals[(point,min(points))] = ComputerState()
            elif isinstance(r, Storage):
                r.intervals[(point,min(points))] = StorageState()
            elif isinstance(r, Router):
                r.intervals[(point,min(points))] = RouterState()
            elif isinstance(r, Link):
                r.intervals[(point,min(points))] = LinkState()
            return
        i = 1
        while points[i] < point:
            i+=1
        r.intervals[(points[i-1],point)] = copy.deepcopy(r.intervals[(points[i-1],points[i])])
        r.intervals[(point,points[i])] = copy.deepcopy(r.intervals[(points[i-1],points[i])])
        del r.intervals[(points[i-1],points[i])]

    def GetCurrentTimePoints(self):
        l = set([])
        for d in self.assignedDemands:
            l.add(d.startTime)
            l.add(d.endTime)
        l = list(l)
        l.sort()
        return l

    def RemoveTimePoint(self, intervals, point):
        points = self.GetCurrentTimePoints()
        if points.count(point) != 0:
            return
        points = []
        for k in intervals.keys():
            points.extend([k[0],k[1]])
        points = list(set(points))
        points.remove(point)
        points.sort()
        if point > max(points):
            del intervals[(max(points),point)]
            return
        if point < min(points):
            del intervals[(point,min(points))]
            return
        i = 1
        while points[i] < point:
            i+=1
        intervals[(points[i-1],points[i])] = copy.deepcopy(intervals[(points[i-1],point)])
        del intervals[(points[i-1],point)]
        del intervals[(point,points[i])]

    def PrepareIntervals(self, demand):
        for v in self.vertices:
            if v.intervals == {}:
                if isinstance(v, Computer):
                    v.intervals[(demand.startTime,demand.endTime)] = ComputerState()
                elif isinstance(v, Storage):
                    v.intervals[(demand.startTime,demand.endTime)] = StorageState()
                elif isinstance(v, Router):
                    v.intervals[(demand.startTime,demand.endTime)] = RouterState()
            else:
                self.AddTimePoint(v, demand.startTime)
                self.AddTimePoint(v, demand.endTime)
        for e in self.edges:
            if e.intervals == {}:
                e.intervals[(demand.startTime,demand.endTime)] = LinkState()
            else:
                self.AddTimePoint(e, demand.startTime)
                self.AddTimePoint(e, demand.endTime)

    def LoadAssignedDemand(self, demand):
        self.PrepareIntervals(demand)
        ranges = self.GetRanges(demand)
        for time in ranges:
            for v in demand.vertices:
                self.AssignVertex(demand, v, v.resource, time)
            for e in demand.edges:
                if e.e1.resource == e.e2.resource:
                    continue
                self.AssignLink(demand, e, e.path, time)
            for r in demand.replications:
                self.AssignReplica(demand, r, time)
            for rl in demand.replicalinks:
                self.AssignReplicaLink(demand, rl, rl.path, time)

    def LoadAllDemands(self, demands):
        points = set([])
        for demand in demands:
            if demand.assigned:
                points.add(demand.startTime)
                points.add(demand.endTime)
        points = list(points)
        points.sort()
        ranges = []
        for i in range(0,len(points)-1):
            ranges.append((points[i],points[i+1]))
        for v in self.vertices:
            v.intervals = {}
            for r in ranges:
                if isinstance(v, Computer):
                    v.intervals[r] = ComputerState()
                elif isinstance(v, Storage):
                    v.intervals[r] = StorageState()
                elif isinstance(v, Router):
                    v.intervals[r] = RouterState()
        for e in self.edges:
            e.intervals = {}
            for r in ranges:
                e.intervals[r] = LinkState()
        for demand in demands:
            if demand.assigned:
                r = self.GetRanges(demand)
                for t in r:
                    for v in demand.vertices:
                        self.AssignVertex(demand,v,v.resource,t)
                    for e in demand.edges:
                        if e.e1.resource == e.e2.resource:
                            continue
                        self.AssignLink(demand, e, e.path, t)
                    for r in demand.replications:
                        self.AssignReplica(demand,r,t)
                    for rl in demand.replicalinks:
                        self.AssignReplicaLink(demand, rl, rl.path, t)

    def RemoveIntervals(self, demand):
        for v in self.vertices:
            if len(v.intervals.keys())==1:
                del v.intervals[(demand.startTime,demand.endTime)]
            else:
                self.RemoveTimePoint(v.intervals, demand.startTime)
                self.RemoveTimePoint(v.intervals, demand.endTime)
        for e in self.edges:
            if len(e.intervals.keys())==1:
                del e.intervals[(demand.startTime,demand.endTime)]
            else:
                self.RemoveTimePoint(e.intervals, demand.startTime)
                self.RemoveTimePoint(e.intervals, demand.endTime)

    def GenerateTree3(self, params):
        copyNum=params["copyNum"] + 1
        leafwidth = 25
        leafNumber = params["computersNum"]*params["computersNodes"] + params["storagesNum"]*params["storagesNodes"]
        width = leafNumber*leafwidth
        num0 = num1 = num2 = num3 = 0
        for i in range(params["routersNum0"]):
            w = width / params["routersNum0"]/copyNum
            routers0=[]
            for j in range(copyNum):
                r = Router("router_0_"+str(num0), params["routerBandwidth0"])
                r.x = 15 + 0.5*w + num0*w
                r.y = 15
                self.AddVertex(r)
                routers0.append(r)
                num0+=1
            for j in range(params["routerChilds0"]):
                w1 = width / params["routerChilds0"]/params["routersNum0"]/copyNum
                childs1 = []
                for k in range(copyNum):
                    child1 = Router("router_1_"+str(num1), params["routerBandwidth1"])
                    child1.x = 15 + 0.5*w1 + num1*w1
                    child1.y = 15 + 2*leafwidth
                    self.AddVertex(child1)
                    num1 += 1
                    for r in routers0:
                        channel1 = Link(r,child1,params["channelsBandwidth0"])
                        self.AddLink(channel1)
                    childs1.append(child1)
                for k in range(params["computersNodes"]/params["routerChilds0"]/params["routersNum0"]):
                    w2 = width / (params["routerChilds1"]*params["routerChilds0"]*params["routersNum0"])
                    child2 = Router("router_2_"+str(num2), params["routerBandwidth2"])
                    child2.x = 15 + 0.5*w2 + num2*w2
                    child2.y = 15 + 4*leafwidth
                    self.AddVertex(child2)
                    for child1 in childs1:
                        channel2 = Link(child1,child2,params["channelsBandwidth1"])
                        self.AddLink(channel2)
                    for l in range(params["computersNum"]):
                        computer = Computer("computer"+str(num3), params["performance"], params["ram"])
                        computer.x = 15 + 0.5*leafwidth + num3*leafwidth
                        computer.y = 15 + 6*leafwidth
                        self.AddVertex(computer)
                        channel3 = Link(child2,computer,params["computerChannelsBandwidth2"])
                        self.AddLink(channel3)
                        num3+=1
                    num2+=1
                for k in range(params["storagesNodes"]/params["routerChilds0"]/params["routersNum0"]):
                    w2 = width / (params["routerChilds1"]*params["routerChilds0"]*params["routersNum0"])
                    child2 = Router("router_2_"+str(num2), params["routerBandwidth2"])
                    child2.x = 15 + 0.5*w2 + num2*w2
                    child2.y = 15 + 4*leafwidth
                    self.AddVertex(child2)
                    for child1 in childs1:
                        channel2 = Link(child1,child2,params["channelsBandwidth1"])
                        self.AddLink(channel2)
                    for l in range(params["storagesNum"]):
                        storage = Storage("storage"+str(num3),params["capacity"],random.randint(0,params["numTypes"]-1))
                        storage.x = 15 + 0.5*leafwidth + num3*leafwidth
                        storage.y = 15 + 6*leafwidth
                        self.AddVertex(storage)
                        channel3 = Link(child2,storage,params["storageChannelsBandwidth2"])
                        self.AddLink(channel3)
                        num3+=1
                    num2+=1

    def GenerateTree2(self, params):
        copyNum = params["copyNum"] + 1
        leafwidth = 25
        leafNumber = params["computersNum"]*params["computersNodes"] + params["storagesNum"]*params["storagesNodes"]
        width = leafNumber*leafwidth
        num0 = num1 = num2 = 0
        for i in range(params["routersNum0"]):
            w = width / params["routersNum0"]/copyNum
            routers0 = []
            for j in range(copyNum):
                r = Router("router_0_"+str(num0), params["routerBandwidth0"])
                r.x = 15 + 0.5*w + num0*w
                r.y = 15
                self.AddVertex(r)
                routers0.append(r)
                num0+=1
            for k in range(params["computersNodes"]/params["routersNum0"]):
                w2 = width / (params["routerChilds0"]*params["routersNum0"])
                child1 = Router("router_1_"+str(num1), params["routerBandwidth2"])
                child1.x = 15 + 0.5*w2 + num1*w2
                child1.y = 15 + 2*leafwidth
                self.AddVertex(child1)
                for r in routers0:
                    channel1 = Link(child1,r,params["channelsBandwidth1"])
                    self.AddLink(channel1)
                for l in range(params["computersNum"]):
                    computer = Computer("computer"+str(num2), params["performance"], params["ram"])
                    computer.x = 15 + 0.5*leafwidth + num2*leafwidth
                    computer.y = 15 + 4*leafwidth
                    self.AddVertex(computer)
                    channel2 = Link(child1,computer,params["computerChannelsBandwidth2"])
                    self.AddLink(channel2)
                    num2+=1
                num1+=1
            for k in range(params["storagesNodes"]/params["routersNum0"]):
                w2 = width / (params["routerChilds0"]*params["routersNum0"])
                child1 = Router("router_1_"+str(num1), params["routerBandwidth2"])
                child1.x = 15 + 0.5*w2 + num1*w2
                child1.y = 15 + 2*leafwidth
                self.AddVertex(child1)
                for r in routers0:
                    channel1 = Link(child1,r,params["channelsBandwidth1"])
                    self.AddLink(channel1)
                for l in range(params["storagesNum"]):
                    storage = Storage("storage"+str(num2),params["capacity"],random.randint(0,params["numTypes"]-1))
                    storage.x = 15 + 0.5*leafwidth + num2*leafwidth
                    storage.y = 15 + 4*leafwidth
                    self.AddVertex(storage)
                    channel2 = Link(child1,storage,params["storageChannelsBandwidth2"])
                    self.AddLink(channel2)
                    num2+=1
                num1+=1

    def GenerateCommonStructure(self, params):
        copyNum=params["copyNum"] + 1
        leafwidth = 25
        leafNumber = params["computersNum"]*params["computersNodes"] + params["storagesNum"]*params["storagesNodes"]
        width = leafNumber*leafwidth
        rootRouters = []
        for i in range(params["routersNum0"]):
            w = width / params["routersNum0"]
            r = Router("router_0_"+str(i), params["routerBandwidth0"])
            r.x = 15 + 0.5*w + i*w
            r.y = 15
            self.AddVertex(r)
            rootRouters.append(r)
        num1 = num2 = num3 = 0
        for i in range(params["routersNum1"]):
            w1 = width / params["routersNum1"]/copyNum
            childs1 = []
            for j in range(copyNum):
                child1 = Router("router_1_"+str(num1), params["routerBandwidth1"])
                child1.x = 15 + 0.5*w1 + num1*w1
                child1.y = 15 + 2*leafwidth
                self.AddVertex(child1)
                childs1.append(child1)
                num1+=1
            for r in rootRouters:
                for child1 in childs1:
                    channel1 = Link(r,child1,params["channelsBandwidth0"])
                    self.AddLink(channel1)
            for k in range(params["computersNodes"]/params["routersNum1"]):
                w2 = width / (params["routerChilds1"]*params["routersNum1"])
                child2 = Router("router_2_"+str(num2), params["routerBandwidth2"])
                child2.x = 15 + 0.5*w2 + num2*w2
                child2.y = 15 + 4*leafwidth
                self.AddVertex(child2)
                for child1 in childs1:
                    channel2 = Link(child1,child2,params["channelsBandwidth1"])
                    self.AddLink(channel2)
                for l in range(params["computersNum"]):
                    computer = Computer("computer"+str(num3), params["performance"], params["ram"])
                    computer.x = 15 + 0.5*leafwidth + num3*leafwidth
                    computer.y = 15 + 6*leafwidth
                    self.AddVertex(computer)
                    channel3 = Link(child2,computer,params["computerChannelsBandwidth2"])
                    self.AddLink(channel3)
                    num3+=1
                num2+=1
            for k in range(params["storagesNodes"]/params["routersNum1"]):
                w2 = width / (params["routerChilds1"]*params["routersNum1"])
                child2 = Router("router_2_"+str(num2), params["routerBandwidth2"])
                child2.x = 15 + 0.5*w2 + num2*w2
                child2.y = 15 + 4*leafwidth
                self.AddVertex(child2)
                for child1 in childs1:
                    channel2 = Link(child1,child2,params["channelsBandwidth1"])
                    self.AddLink(channel2)
                for l in range(params["storagesNum"]):
                    storage = Storage("storage"+str(num3),params["capacity"],random.randint(0,params["numTypes"]-1))
                    storage.x = 15 + 0.5*leafwidth + num3*leafwidth
                    storage.y = 15 + 6*leafwidth
                    self.AddVertex(storage)
                    channel3 = Link(child2,storage,params["storageChannelsBandwidth2"])
                    self.AddLink(channel3)
                    num3+=1
                num2+=1
