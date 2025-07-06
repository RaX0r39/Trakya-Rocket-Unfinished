import tkinter as tk
from tkinter import ttk, scrolledtext
import random
import threading
import time
from datetime import datetime

class RocketGroundStation:
    def __init__(self, root):
        self.root = root
        self.root.title("Roket Yer İstasyonu - Test")
        self.root.geometry("800x600")
        
        # Test verileri
        self.telemetry_data = {
            'sicaklik': 25.0,
            'ivme': 0.0,
            'gps_lat': 41.0082,
            'gps_lon': 28.9784,
            'yukseklik': 0.0
        }
        
        # Test simülasyonu
        self.test_running = False
        
        self.setup_ui()
        self.start_test_data()
        self.update_display()
        
    def setup_ui(self):
        # Başlık
        title_label = tk.Label(self.root, text="Roket Test Yer İstasyonu", 
                              font=('Arial', 16, 'bold'))
        title_label.pack(pady=10)
        
        # Test kontrolü
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        self.start_btn = tk.Button(control_frame, text="Test Başlat", 
                                  command=self.start_test_data, width=12)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(control_frame, text="Test Durdur", 
                                 command=self.stop_test_data, width=12)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Telemetri verileri
        data_frame = tk.LabelFrame(self.root, text="Telemetri Verileri", font=('Arial', 12))
        data_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Sıcaklık
        temp_frame = tk.Frame(data_frame)
        temp_frame.pack(fill=tk.X, pady=5, padx=10)
        tk.Label(temp_frame, text="Sıcaklık:", font=('Arial', 10)).pack(side=tk.LEFT)
        self.temp_label = tk.Label(temp_frame, text="25.0 °C", font=('Arial', 10, 'bold'))
        self.temp_label.pack(side=tk.RIGHT)
        
        # İvme
        ivme_frame = tk.Frame(data_frame)
        ivme_frame.pack(fill=tk.X, pady=5, padx=10)
        tk.Label(ivme_frame, text="İvme:", font=('Arial', 10)).pack(side=tk.LEFT)
        self.ivme_label = tk.Label(ivme_frame, text="0.0 m/s²", font=('Arial', 10, 'bold'))
        self.ivme_label.pack(side=tk.RIGHT)
        
        # Yükseklik
        yukseklik_frame = tk.Frame(data_frame)
        yukseklik_frame.pack(fill=tk.X, pady=5, padx=10)
        tk.Label(yukseklik_frame, text="Yükseklik:", font=('Arial', 10)).pack(side=tk.LEFT)
        self.yukseklik_label = tk.Label(yukseklik_frame, text="0.0 m", font=('Arial', 10, 'bold'))
        self.yukseklik_label.pack(side=tk.RIGHT)
        
        # GPS
        gps_frame = tk.LabelFrame(data_frame, text="GPS Konum", font=('Arial', 10))
        gps_frame.pack(fill=tk.X, pady=10, padx=10)
        
        lat_frame = tk.Frame(gps_frame)
        lat_frame.pack(fill=tk.X, pady=2, padx=5)
        tk.Label(lat_frame, text="Enlem:", font=('Arial', 10)).pack(side=tk.LEFT)
        self.lat_label = tk.Label(lat_frame, text="41.008200", font=('Arial', 10, 'bold'))
        self.lat_label.pack(side=tk.RIGHT)
        
        lon_frame = tk.Frame(gps_frame)
        lon_frame.pack(fill=tk.X, pady=2, padx=5)
        tk.Label(lon_frame, text="Boylam:", font=('Arial', 10)).pack(side=tk.LEFT)
        self.lon_label = tk.Label(lon_frame, text="28.978400", font=('Arial', 10, 'bold'))
        self.lon_label.pack(side=tk.RIGHT)
        
        # Log
        log_frame = tk.LabelFrame(self.root, text="Log", font=('Arial', 12))
        log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, font=('Courier', 9))
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def start_test_data(self):
        if not self.test_running:
            self.test_running = True
            self.test_thread = threading.Thread(target=self.generate_test_data)
            self.test_thread.daemon = True
            self.test_thread.start()
            self.log_message("Test verisi başlatıldı")
    
    def stop_test_data(self):
        self.test_running = False
        self.log_message("Test verisi durduruldu")
    
    def generate_test_data(self):
        while self.test_running:
            # Basit rastgele veriler
            self.telemetry_data['sicaklik'] = random.uniform(20, 35)
            self.telemetry_data['ivme'] = random.uniform(-5, 15)
            self.telemetry_data['yukseklik'] = random.uniform(0, 1000)
            self.telemetry_data['gps_lat'] = 41.0082 + random.uniform(-0.001, 0.001)
            self.telemetry_data['gps_lon'] = 28.9784 + random.uniform(-0.001, 0.001)
            
            time.sleep(0.5)  # Yarım saniyede bir güncelle
    
    def update_display(self):
        # Verileri güncelle
        self.temp_label.config(text=f"{self.telemetry_data['sicaklik']:.1f} °C")
        self.ivme_label.config(text=f"{self.telemetry_data['ivme']:.1f} m/s²")
        self.yukseklik_label.config(text=f"{self.telemetry_data['yukseklik']:.1f} m")
        self.lat_label.config(text=f"{self.telemetry_data['gps_lat']:.6f}")
        self.lon_label.config(text=f"{self.telemetry_data['gps_lon']:.6f}")
        
        # Her 100ms'de bir güncelle
        self.root.after(100, self.update_display)
    
    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, full_message)
        self.log_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RocketGroundStation(root)
    root.mainloop()