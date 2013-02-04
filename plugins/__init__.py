from lxml import etree
import sys

class ParserError:
    @staticmethod
    def parse_error(message):
        raise Exception(message)
    
    @staticmethod
    def invalid_element(tag, line, inside=None):
        error_msg = 'Invalid element <' + tag + '> found at line ' + str(line)
        if inside != None:
            error_msg = error_msg + ' inside <' + inside + '>'
            
        ParserError.parse_error(error_msg)
    
    @staticmethod
    def incomplet_element(tag, line, elements):
        error_msg = 'An incomplete element <' + tag + '> was found  at line ' + str(line) + '.\n'
        error_msg = error_msg + 'It must have: '
        for elem in elements:
            error_msg = error_msg + '<' + elem + '> '
            
        ParserError.parse_error(error_msg)            
    
    @staticmethod      
    def attribute_missing(tag, attribute, line):
        error_msg = 'The attribute "'+ attribute + '" from element <' + tag + \
                '> is missing at line ' + str(line) + '.\n'
            
        ParserError.parse_error(error_msg)           
        
    @staticmethod
    def invalid_attribute(tag, attribute, value, line):
        error_msg = 'The attribute "'+ attribute + '" from element <' + tag + \
                '> has the invalid value "' + value + '" at line ' + str(line) + '.\n'
            
        ParserError.parse_error(error_msg)  

class PluginsManager:
    def __init__(self):
        self.__annotation_plugins = {}
        
    def add_annotation_plugin(self, ann_type, module_name, class_name):
        if self.__annotation_plugins.has_key(ann_type):
            raise Exception("There is another annotation with this type known.")
        
        if module_name == None:
            module_name = ann_type
        if class_name == None:
            class_name = ann_type
            
        self.__annotation_plugins[ann_type] = (module_name, class_name)
    
    def load_file(self, filename):
        mfile = open(filename, 'r')
        tree = etree.parse(mfile)
        root = tree.getroot();
        
        if root.tag != 'AnnotatorPlugins':
            self._parse_err or('Root element must be <AnnotatorPlugins>')
            
        childs = root.iterchildren()
        for elem in childs:
            if type (elem) != etree._Element:
                #just a comment
                continue
            
            if elem.tag == 'AnnotationBas':
                self.parse_annotation_base(elem)
            else:
                ParserError.invalid_element(elem.tag, elem.sourceline)
                
                
    def parse_annotation_base(self, xml_base):
        childs = xml_base.iterchildren()
        for elem in childs:
            if type (elem) != etree._Element:
                #just a comment
                continue
            
            if elem.tag == 'Annotation':
                self.parse_annotation_plugin(elem)
            else:
                ParserError.invalid_element(elem.tag, elem.sourceline)
                
    def parse_annotation_plugin(self, xml_note):
        ann_type = xml_note.get('type')
        if ann_type == None:
            ParserError.attribute_missing(xml_note.tag, 'type', xml_note.sourceline)
            
        module_name = xml_note.find('module')
        class_name = xml_note.find('class')
        
        if module_name == None or class_name == None:
            ParserError.incomplet_element(xml_note.tag, xml_note.sourceline, 
                                          ['module', 'class'])
            
        self.add_annotation_plugin(ann_type, module_name.text, class_name.text)
        
        
    def get_annotation_class(self, ann_type):
        if not self.__annotation_plugins.has_key(ann_type):
            raise IndexError('There is no %s type of annotation known' % ann_type)
        
        model_name, class_name = self.__annotation_plugins[ann_type]
        __import__('plugins.' + model_name)
        mymodule = sys.modules['plugins.' + model_name]
        myclass = mymodule.__dict__[class_name]
        return myclass
    
def test():
    plugins_manager = PluginsManager()
    plugins_manager.load_file('plugins.xml')
    

if __name__ == "__main__":
    test()
    
        
        