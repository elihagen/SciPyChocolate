import os
import ipywidgets as widgets
from IPython.display import display




class Best_fitting_chocolate:

    
    

    def __init__(self, df):
        self.df_in = df
        self.df = df
        self.next = False
        self.all_widget = widgets.Checkbox(description='select all', value=True)
        
        first_message = widgets.HTML(
            value="<b>This is your personal chocolate finder, select all properties your chocolate should possess and get your favorite chocolate :)</b>",
            # placeholder='Some HTML',
            # description='Some HTML',
        )
        
       
        
        cocoa_min = min(self.df_in["cocoa percent"])
        cocoa_max = max(self.df_in["cocoa percent"])
        self.w = widgets.FloatRangeSlider(
            value=[cocoa_min, cocoa_max],
            min=cocoa_min,
            max=cocoa_max,
            step=1,
            description='Cocoa percent:',
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='.1f',
        )
        self.countries = set(self.df_in['country of bean origin'])
        self.options_dict = {description: widgets.Checkbox(description=description, value=True) for description in self.countries}
        options = [self.options_dict[description] for description in self.countries]
        options_widget = widgets.VBox(options, layout={'overflow': 'scroll'})
        bean_origin = widgets.VBox([self.all_widget, options_widget])
        
        self.ingredients = ('cocoa butter','vanilla','lecithin','salt','sugar','sweetener without sugar')
        self.ingredients_dict = {description: widgets.Checkbox(description=description, value=False) for description in self.ingredients}
        options = [self.ingredients_dict[description] for description in self.ingredients]
        show_ingredients = widgets.VBox(options, layout={'overflow': 'scroll'})
       
        self.allergies_dict = {description: widgets.Checkbox(description=description, value=False) for description in self.ingredients}
        options = [self.allergies_dict[description] for description in self.ingredients]
        show_ingredients2 = widgets.VBox(options, layout={'overflow': 'scroll'})
        
        accordion = widgets.Accordion(children=[self.w,bean_origin,show_ingredients, show_ingredients2])
        accordion.set_title(0,'Choose your cocoa percent!')
        accordion.set_title(1, 'From which countries should your cocoa beans be?')
        accordion.set_title(2, 'Which ingredients do you like?')
        accordion.set_title(3, 'Do you have any allergies or ingredients you do not want to have in your chocolate?')
        


        # button = widgets.ToggleButton(
        #     value=False,
        #     description='Continue',
        #     disabled=False,
        #     button_style='', # 'success', 'info', 'warning', 'danger' or ''
        #     tooltip='Description',
        #      # (FontAwesome names without the `fa-` prefix)
        # )
        self.end_message = widgets.HTML(value="")
        file = open("chocolade.picture.png", "rb")
        image = file.read()
        picture=widgets.Image(
            value=image,
            format='png',
            width=300,
            height=400,
        )
        file = open("chocolate.questionmark.jpg", "rb")
        image = file.read()
        picture2=widgets.Image(
            value=image,
            format='png',
            width=150,
            height=200,
        )
        
        display(first_message)
        display(picture)
        display(accordion)
        
        self.button = widgets.Button(description="Get your favourite chocolate(s)",
                                     layout=widgets.Layout(width='50%', height='50px'),
                                     button_style='success')
        
        self.button2 = widgets.Button(description="Next",
                                     layout=widgets.Layout(width='50%', height='50px'),
                                     button_style='info')
        self.button_back = widgets.Button(description="Back",
                                     layout=widgets.Layout(width='50%', height='50px'),
                                     button_style='info')
        display(self.button)
        self.button.on_click(self.on_button_clicked)

        display(self.end_message)
        self.button2.layout.visibility = "hidden"
        self.button_back.layout.visibility = "hidden"
        display(self.button_back)
        display(self.button2)
        display(picture2)
        

      
        
        
    def on_button_clicked(self,b):
        # with output:
        #     print("Button clicked.")
        
        self.prüf = True
    
        cocoa_min = self.w.value[0]
        cocoa_max = self.w.value[1]

        
        self.df = self.df_in[self.df_in['cocoa percent'] >= cocoa_min]
        self.df = self.df[self.df['cocoa percent'] <= cocoa_max]
        
        if not(self.df.empty):
            if not(self.all_widget.value):
                for description in self.countries:
                    if not(self.options_dict[description].value):
                        self.df = self.df[self.df['country of bean origin'] != description]
                        
                        #('cocoa butter','vanilla','lecithin','salt,sugar','sweetener without sugar')
                        
       
        for description in self.ingredients:
            if not(self.df.empty):
                if self.ingredients_dict[description].value:
                    self.df = self.df[self.df[description] == 'have ' + description]
                if self.allergies_dict[description].value:
                    self.df = self.df[self.df[description] == 'have not ' + description]

                        
        if self.df.empty:
            self.end_message.value = "Your favorite chocolate unfortunately doesn't exist, try to be a bit more general!"
            self.button2.layout.visibility = "hidden"
            self.button_back.layout.visibility = "hidden"
            self.button.on_click(self.on_button_clicked)
                  
        else:
            self.next = False
            self.zaehler = 0
            self.anzahl = len(self.df)
            self.df.index = range(0,self.anzahl)
            self.button_back.layout.visibility = "hidden"

            self.on_button2_clicked(True)
            
    def on_button2_clicked(self,b):
            #for threads: could be errors because threads are concurrently
            if self.zaehler < self.anzahl:
                self.zaehler = self.zaehler + 1
            
            ingredients = "beans"
            for i in self.ingredients:
                if self.df[i][self.zaehler - 1] == "have " + i:
                    ingredients = ingredients + ", " + i
                
                
            tastes = self.df['first taste'][self.zaehler - 1]
            if self.df['second taste'][self.zaehler - 1] != "no information":
                tastes = tastes + ", " + self.df['second taste'][self.zaehler - 1]
            if self.df['third taste'][self.zaehler - 1] != "no information":
                tastes = tastes + ", " + self.df['third taste'][self.zaehler - 1]    
           
            self.end_message.value = "<br><b>Your best chocolate(s):</b><br><br><b>Rating:</b>  " + str(self.df['rating'][self.zaehler - 1]) + "<br><b>Country of bean origin:</b>  " + self.df['country of bean origin'][self.zaehler - 1] + "<br><b>Cocoa percent:</b>  " + str(self.df['cocoa percent'][self.zaehler - 1]) + "<br><b>Taste:</b>  " + tastes + "<br><b>Ingredients:</b>  " + ingredients + "<br><b>Company:</b>  " + self.df['company'][self.zaehler - 1] + "<br><b>Company Location:</b>  " + self.df['company location'][self.zaehler - 1] + "<br><br>Chocolate " + str(self.zaehler) + "/" + str(self.anzahl) 
            
            
            if self.anzahl > self.zaehler:

                #self.df = self.df[1:self.anzahl]
                if not(self.next):
                    self.next = True
                    self.button2.layout.visibility = "visible"
                    

                #self.zaehler = self.zaehler + 1               
                self.button2.on_click(self.on_button2_clicked)
            else: self.button2.layout.visibility = "hidden"

            if self.zaehler > 1:
                self.button_back.layout.visibility = "visible"
                self.button_back.on_click(self.on_button_back_clicked) 
                
            self.button.on_click(self.on_button_clicked)  
          

    def on_button_back_clicked(self,b):
        #for threads
        if self.zaehler > 1:
            self.zaehler = self.zaehler - 2
            
        if self.zaehler == 0:
            self.button_back.layout.visibility = "hidden"
            self.next = False
        self.on_button2_clicked(True)
       



        
        
  