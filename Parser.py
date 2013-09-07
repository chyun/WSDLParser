from WebService import WebService
from xml.dom import minidom, Node
from xml.dom.minidom import parseString
class Parser:
    def __init__(self):
        pass;
    def parse(self, wsdlFile):
        ws = WebService();
        xmlFile = minidom.parse(wsdlFile);

        operations = None;
        #parse web service name
        service = xmlFile.getElementsByTagName('wsdl:service');
        if service.length > 0:
            ws.name = service[0].getAttribute('name');
            port = service[0].getElementsByTagName('wsdl:port');
            bindingName = port[0].getAttribute('binding');
            start = bindingName.find(':');
            bindingName = bindingName[start + 1 : ];
            bindings = xmlFile.getElementsByTagName('wsdl:binding');
            binding = self.findBinding(bindingName, bindings);
            bindingTypeName = binding.getAttribute('type');
            start = bindingTypeName.find(':');
            bindingTypeName = bindingTypeName[start + 1 : ];
            portTypes = xmlFile.getElementsByTagName('wsdl:portType');
            portType = self.findPortType(bindingTypeName, portTypes);
            operations = xmlFile.getElementsByTagName('wsdl:operation');
        else:
            operations = xmlFile.getElementsByTagName('wsdl:operation');
        
        #print operations;
        opration = '';
        if(operations.length >= 0):
            operation = operations[0];
            #print operation;
        else:
            return ws;

        #print operation
        inputMessage = operation.getElementsByTagName('wsdl:input');
        #print inputMessage;
        messageName = inputMessage[0].getAttribute('message');

        #get rid of the prefix
        start = messageName.find(":");
        messageName = messageName[start + 1 : ];
        
        #print messageName;
        messages = xmlFile.getElementsByTagName('wsdl:message');
##        print messages;
        
        message =  self.findMessage(messageName, messages);
        parts = message.getElementsByTagName('wsdl:part');
        elements = xmlFile.getElementsByTagName('s:element');
        #find input paras
        #inputs = {};
        for part in parts:
            elementName = part.getAttribute('element');
            start = elementName.find(":");
            elementName = elementName[start + 1 : ];
            #print elementName;
            element = self.findElement(elementName, elements);
            #print element;
            self.findParasInElem(element, ws.inputList);

        print ws.inputList;

        #find output paras
        outputMessage = operation.getElementsByTagName('wsdl:output');
        messageName = outputMessage[0].getAttribute('message');
        #print messageName;
        start = messageName.find(":");
        messageName = messageName[start + 1 : ];
        message =  self.findMessage(messageName, messages);
        parts = message.getElementsByTagName('wsdl:part');

        elements = xmlFile.getElementsByTagName('s:element');
        for part in parts:
            elementName = part.getAttribute('element');
            start = elementName.find(":");
            elementName = elementName[start + 1 : ];
            #print elementName;
            element = self.findElement(elementName, elements);
            #print element;
            self.findParasInElem(element, ws.outputList);

        print ws.outputList;
        print ws.name;
       
    def findMessage(self, messageName, messages):
        for message in messages:
            node_name = message.getAttribute('name');
            #print node_name;
            if(node_name == messageName):
                return message;
        return None;

    def findElement(self, elementName, elements):
        for element in elements:
            node_name = element.getAttribute('name');
            if(node_name == elementName):
                return element;
        return None;

    def findParasInElem(self, element, paras):
        subElems = element.getElementsByTagName('s:element');
        #paras = {}
        for subElem in subElems:
            para = subElem.getAttribute('name');
            paraType = subElem.getAttribute('type');
            start = paraType.find(":");
            paraType = paraType[start + 1 : ];
            paras[para.lower()] = paraType;

    def findBinding(self, bindingName, bindings):
        for binding in bindings:
            bind_name = binding.getAttribute('name');
            if bind_name == bindingName:
                return binding;
        return None;

    def findPortType(self, bindingTypeName, portTypes):
        for portType in portTypes:
            portType_name = portType.getAttribute('name');
            if portType_name == bindingTypeName:
                return portType;

        return None;
        
        #return paras;
        

        
        

        

