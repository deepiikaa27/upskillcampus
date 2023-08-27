from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class EnergyMonitoringApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.energy_label = Label(text="Energy Consumption: 0 kWh")
        self.layout.add_widget(self.energy_label)
        
        self.update_button = Button(text="Update Data", on_press=self.update_energy)
        self.layout.add_widget(self.update_button)
        
        return self.layout
    
    def update_energy(self, instance):
        # Simulate fetching energy data from a device or API
        energy_data = random.uniform(0, 10)  # Simulate energy data between 0 and 10 kWh
        self.energy_label.text = f"Energy Consumption: {energy_data:.2f} kWh"

if __name__ == '__main__':
    EnergyMonitoringApp().run()
    