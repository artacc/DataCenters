#ifndef NETWORKINGELEMENT_H
#define NETWORKINGELEMENT_H

#include "element.h"

#include <string>
using std::string;

class NetworkingElement : public Element {
protected:
    NetworkingElement(string name = "unnamed_networking_element"
        , unsigned long capacity = 0, unsigned long max = 0)
    : Element(name, capacity, max)
    {
        setType(Element::NETWORKING);
    }
};

#endif // NETWORKINGELEMENT_H
