from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import gps

class GPSApp(App):
    def build(self):
        self.box_layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.permission_label = Label(text='Menggunakan GPS memerlukan izin. Izinkan?')
        self.allow_button = Button(text='Izinkan GPS')
        self.allow_button.bind(on_release=self.get_location)
        
        self.location_label = Label(text='Latitude: -\nLongitude: -')
        self.get_location_button = Button(text='Dapatkan Lokasi Terkini')
        self.get_location_button.bind(on_release=self.get_location)
        
        self.box_layout.add_widget(self.permission_label)
        self.box_layout.add_widget(self.allow_button)
        self.box_layout.add_widget(self.location_label)
        self.box_layout.add_widget(self.get_location_button)
        
        return self.box_layout

    def get_location(self, instance):
        if instance == self.allow_button:
            gps.configure(on_location=self.on_location)
            gps.start()
        elif instance == self.get_location_button:
            gps.start()

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        self.location_label.text = f'Latitude: {lat:.6f}\nLongitude: {lon:.6f}'

if __name__ == '__main__':
    GPSApp().run()
