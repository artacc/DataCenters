#ifndef INTERNALGRAPH_H
#define INTERNALGRAPH_H

#include <vector>
#include <set>
#include "path.h"

// Class representing a single arc in the graph
struct Arc
{
    double pher;
    double heur;

    Arc()
    : pher(0)
    , heur(0)
    {}

    Arc(double p, double h)
    : pher(p)
    , heur(h)
    {}

    Arc(const Arc & a);
    Arc& operator=(const Arc & a);
    // default destructor
};

// Class representing a vertex in the graph that corresponds to one of the requests
// Also manages arcs to the vertices representing physical resources
class GraphComponent
{
public:
    typedef enum {NOTYPE = 0, VMACHINE = 1, STORAGE = 2} RequestType;

    GraphComponent(unsigned long req, int phys, RequestType t, unsigned int sType = 0);
    ~GraphComponent();

    GraphComponent(const GraphComponent & gc);
    GraphComponent& operator=(const GraphComponent & gc);

    unsigned int getResNum() const { return physArcs.size(); }
    RequestType getType() const { return type; }
    unsigned long getRequired () const { return required; }
    bool isCreated() const { return success; }

    // Perform some actions when a new path is about to start building
    void nextPath();
    // Init pheromone and heuristic values
    void initValues(std::vector<unsigned long> & res, std::vector<unsigned long> & cap, std::vector<unsigned int> & types);
    // Update heuristic on arcs
    void updateHeuristic(unsigned int resNum, unsigned int resCur, unsigned int resCap);
    // Update pheromone on the arc
    void updatePheromone(unsigned int res, double value);
    // Choose resource for the request
    unsigned int chooseResource(double pherDeg, double heurDeg);
private:
    // initialize
    bool init(int num);

    // Arcs to physical resources
    std::vector<Arc*> physArcs;
    // Initial heuristic values
    std::vector<double> physHeurs;
    // was init() successful?
    bool success;
    // request type
    RequestType type;
    // requested resources
    unsigned long required;
    // storage type
    unsigned int storageType;

    // No default constructor
    GraphComponent();
};

// Ant algorithm internal graph
// Manages pheromone and heuristic values, builds paths
class InternalGraph
{
public:
    InternalGraph(unsigned int nodes, unsigned int stores, unsigned int vm, unsigned int st,
                  std::vector<unsigned long> & res, std::vector<unsigned long> & cap, std::vector<unsigned long> & req,
                  std::vector<unsigned int> & types, std::vector<unsigned int> & reqTypes);
    ~InternalGraph();

    bool isCreated() const { return success; }
    // Perform some actions when a new path is about to start building
    void nextPath();
    // Update pheromone
    void updatePheromone(std::vector<AntPath*> & paths, std::vector<double> & objValues);
    // Update heuristic for every graph component
    void updateInternalHeuristic(unsigned int resNum, GraphComponent::RequestType t);
    // From vertex cur, select a new vertex (one of the set members)
    unsigned int selectVertex(AntPath* pt, unsigned int cur, std::set<unsigned int> & available, bool& s);
    // Set heuristic degree and pheromone degree
    void setHeurDeg(double deg) { heurDeg = deg; }
    void setPherDeg(double deg) { pherDeg = deg; }
    // Request erased from path, add the resources back
    void requestErased(int resource, unsigned int request, GraphComponent::RequestType t);
private:
    // initialize
    bool init(std::vector<unsigned long> & res, std::vector<unsigned long> & cap, std::vector<unsigned long> & req,
              std::vector<unsigned int> & reqTypes);
    void clean(int i, int j, int k);
    // calculate heuristic for arcs
    void initValues(std::vector<unsigned long> & req, std::vector<unsigned int> & types);

    // Vertices that correspond to requests
    std::vector<GraphComponent*> vertices;
    // Arcs between these vertices
    std::vector< std::vector<Arc*> > arcs;
    // Current available physical resources for computational nodes (at the start)
    std::vector<unsigned long> nodesRes;
    // Current available physical resources for storages (at the start)
    std::vector<unsigned long> storesRes;
    // Current available physical resources for computational nodes (when the path is being built)
    std::vector<unsigned long> curNodesRes;
    // Current available physical resources for storages (when the path is being built)
    std::vector<unsigned long> curStoresRes;

    // Maximum available physical resources for computational nodes
    std::vector<unsigned long> nodesCap;
    // Maximum available physical resources for storages
    std::vector<unsigned long> storesCap;

    // select parameters
    double pherDeg;
    double heurDeg;

    // graph parameters
    int nodesNum;
    int storesNum;
    int vmNum;
    int stNum;

    // was init() successful?
    bool success;

    // No default constructor, copy constructor and operator=
    InternalGraph();
    InternalGraph(const InternalGraph&);
    InternalGraph& operator=(const InternalGraph&);
};

#endif
