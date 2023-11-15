from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
import re

Window.size= (500,700)


class MyLayout(BoxLayout):
    
    def Numbers_press(self,number):
        num_before=self.ids.cal_input.text
        
        if num_before=="0":
            num_before=""
            self.ids.cal_input.text=""
        
        self.ids.cal_input.text=f"{num_before}{number}"
        
    def remove(self):
        self.ids.cal_input.text=self.ids.cal_input.text[:-1]
    
    def pos_neg(self):
        if "-" not in self.ids.cal_input.text:
            self.ids.cal_input.text=f'-{self.ids.cal_input.text}'
        else:
            self.ids.cal_input.text=self.ids.cal_input.text[1:]
    
    def find_last_operator(self):
        input_string=self.ids.cal_input.text
        operators = ["+", "-", "x", "/", "."]
        last_operator = None

        for char in input_string:
            if char in operators:
                last_operator = char

        return last_operator    
    
    def split_string_by_operators(self):
        input_string=self.ids.cal_input.text
        operators=["+", "-", "x", "/",]
        # Create a regular expression pattern with the list of operators
        pattern = '|'.join(re.escape(operator) for operator in operators)

        # Split the string using the regular expression pattern
        result = re.split(pattern, input_string)

        # Remove empty strings from the result
        result = [item for item in result if item]

        return result

    def math_func(self, sign):
        last_sign=self.find_last_operator()
        operators = ["+", "-", "x", "/", "."]
        string_=self.ids.cal_input.text
        if string_[-1] in operators:
            pass
        else:
            if sign != ".":
                self.ids.cal_input.text+=sign
            else:
                last_num=self.split_string_by_operators()[-1]
                if "." not in last_num:
                    self.ids.cal_input.text+="."
    
    def list_operators_in_string(self):
        operators = ["+", "-", "x", "/"]
        # Create a regular expression pattern with the list of operators
        pattern = '|'.join(re.escape(operator) for operator in operators)

        # Find all occurrences of the pattern in the input string
        input_string=self.ids.cal_input.text
        matches = re.findall(pattern, input_string)

        return matches
        
    def equals(self):
        
        last=self.ids.cal_input.text[-1]
        operators = ["+", "-", "x", "/", "."]
        if last in operators:
            self.ids.cal_input.text[-1]=""
            

        operator_list=   self.list_operators_in_string() 
        numbers=self.split_string_by_operators()
        
        for op in operator_list:
            
            answer=0.0
            n1=float(numbers[0])
            n2=float(numbers[1])
            
            if op == "+":
                answer=n1+n2
                result=[]
                result.append(answer)
                result= result+numbers[2:]
                numbers=result
                
            if op == "-":
                answer=n1-n2
                result=[]
                result.append(answer)
                result= result+numbers[2:]
                numbers=result
                
            if op == "/":
                if n1!=0 and n2!=0:
                    answer=n1/n2
                    result=[]
                    result.append(answer)
                    result= result+numbers[2:]
                    numbers=result
                else:
                    self.ids.cal_input.text="Undifined!"
                    
            
            if op == "x":
                answer=n1*n2
                result=[]
                result.append(answer)
                result= result+numbers[2:]
                numbers=result
        
        self.ids.cal_input.text=str(numbers[0])
                
        
            
            
            
        
        
            
        
        
    def clear(self):
        self.ids.cal_input.text="0"
        
        


class calculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    calculatorApp().run()