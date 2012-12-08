#include <iostream>
#include "../common/network.h"
#include "../common/request.h"
#include "ant.h"
#include "internalgraph.h"

int main(int argc, char *argv[])
{
    Network n;
    Node * n1 = new Node("n0", 1);
    Node * n2 = new Node("n1", 2);
    Node * n3 = new Node("n2", 3);
    Store * s1 = new Store("s0", 10);
    Store * s2 = new Store("s1", 20);
    Store * s3 = new Store("s2", 30);
    Store * s4 = new Store("s3", 40, 40, 1);
    Switch * w1 = new Switch("w0", 10);
    Switch * w2 = new Switch("w1", 10);
    Switch * w3 = new Switch("w2", 10);
    Link * l1 = new Link("n0w0", 30);
    Link * l2 = new Link("n0w2", 30);
    Link * l3 = new Link("n1w2", 30);
    Link * l4 = new Link("n1w1", 40);
    Link * l5 = new Link("n2w2", 50);
    Link * l6 = new Link("w0w1", 60);
    Link * l7 = new Link("w0s0", 70);
    Link * l8 = new Link("w0s1", 80);
    Link * l9 = new Link("w1s2", 90);
    Link * l10 = new Link("w2s0", 100);
    Link * l11 = new Link("w2s1", 110);
    Link * l12 = new Link("w2s2", 120);
//    Link * l13 = new Link("w2s3", 130);
    Link * l14 = new Link("s2s3", 140);
    l1->bindElements(n1,w1);
    l2->bindElements(n1,w3);
    l3->bindElements(n2,w3);
    l4->bindElements(n2,w2);
    l5->bindElements(n3,w3);
    l6->bindElements(w1,w2);
    l7->bindElements(w1,s1);
    l8->bindElements(w1,s2);
    l9->bindElements(w2,s3);
    l10->bindElements(w3,s1);
    l11->bindElements(w3,s2);
    l12->bindElements(w3,s3);
//    l13->bindElements(w3,s4);
    l14->bindElements(s3,s4);
    n.addNode(n1);
    n.addNode(n2);
    n.addNode(n3);
    n.addStore(s1);
    n.addStore(s2);
    n.addStore(s3);
    n.addStore(s4);
    n.addSwitch(w1);
    n.addSwitch(w2);
    n.addSwitch(w3);
    n.addLink(l1);
    n.addLink(l2);
    n.addLink(l3);
    n.addLink(l4);
    n.addLink(l5);
    n.addLink(l6);
    n.addLink(l7);
    n.addLink(l8);
    n.addLink(l9);
    n.addLink(l10);
    n.addLink(l11);
    n.addLink(l12);
//    n.addLink(l13);
    n.addLink(l14);

    Algorithm::Requests r;
    Request * req1 = new Request;
    Request * req2 = new Request;
    Node * vm1 = new Node("", 1);
    Node * vm2 = new Node("", 1);
    Node * vm3 = new Node("", 2);
    Node * vm4 = new Node("", 2);
    Store * st1 = new Store("", 1);
    Store * st2 = new Store("", 1);
    Store * st3 = new Store("", 2);
//    Store * st5 = new Store("", 2);
//    Store * st6 = new Store("", 2);
//    Store * st7 = new Store("", 2);
    Store * st4 = new Store("", 2, 2, 1);
//    Store * st5 = new Store("", 20);
    Link * ch1 = new Link("", 3);
    Link * ch2 = new Link("", 3);
    Link * ch3 = new Link("", 3);
    Link * ch4 = new Link("", 3);
    Link * ch5 = new Link("", 5);
    Link * ch6 = new Link("", 5);
    Link * ch7 = new Link("", 5);
    Link * ch8 = new Link("", 5);
//    Link * ch9 = new Link("", 500);
    ch1->bindElements(vm1, st1);
    ch2->bindElements(vm1, st2);
    ch3->bindElements(vm2, st1);
    ch4->bindElements(vm2, st2);
    ch5->bindElements(vm3, st3);
    ch6->bindElements(vm3, st4);
    ch7->bindElements(vm4, st3);
    ch8->bindElements(vm4, st4);
//    ch9->bindElements(vm4, st4);
    req1->addVirtualMachine(vm1);
    req1->addVirtualMachine(vm2);
    req2->addVirtualMachine(vm3);
    req2->addVirtualMachine(vm4);
    req1->addStorage(st1);
    req1->addStorage(st2);
//    req1->addStorage(st5);
//    req1->addStorage(st6);
//    req1->addStorage(st7);
    req2->addStorage(st3);
    req2->addStorage(st4);
//    req2->addStorage(st5);
    req1->addLink(ch1);
    req1->addLink(ch2);
    req1->addLink(ch3);
    req1->addLink(ch4);
    req2->addLink(ch5);
    req2->addLink(ch6);
    req2->addLink(ch7);
    req2->addLink(ch8);
//    req2->addLink(ch9);
    r.insert(req1);
    r.insert(req2);
    AntAlgorithm alg(&n, r);//, 1, 1, 1, 1, 0.1);
    if (!alg.isCreated()) return 1;
    std::cerr << "Created\n";
    alg.schedule();
    return 0;
}
