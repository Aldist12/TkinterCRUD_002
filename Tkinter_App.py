import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random
import os

class MysticProdiApp:
    def __init__(self, root):
        self.root = root
        self.init_database()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.setup_layout()
        self.add_mystical_effects()
        
    def init_database(self):
        """Initialize SQLite database"""
        self.db_path = "crystal_ball.db"
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crystal_ball (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_peramal TEXT NOT NULL,
                matematika REAL,
                fisika REAL,
                kimia REAL,
                biologi REAL,
                bahasa_indonesia REAL,
                bahasa_inggris REAL,
                sejarah REAL,
                geografi REAL,
                ekonomi REAL,
                sosiologi REAL,
                prediksi_fakultas TEXT,
                rata_rata REAL,
                tanggal_input DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def setup_window(self):
        """Setup window with mystical theme"""
        self.root.title("🔮 Ramalan Nasib Program Studi - Crystal Ball Predictor")
        self.root.geometry("800x1000")
        
        # Dark mystical gradient background
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, True)
        
        # Center window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def setup_styles(self):
        """Setup mystical styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Submit button style
        self.style.configure('Submit.TButton',
                           font=('Papyrus', 14, 'bold'),
                           padding=(25, 15),
                           background='#2e7d32',
                           foreground='#ffffff',
                           borderwidth=2,
                           relief='raised')
        
        # Magical entry style
        self.style.configure('Magic.TEntry',
                           font=('Georgia', 10),
                           padding=6,
                           fieldbackground='#2e1065',
                           foreground='#e1bee7',
                           borderwidth=2,
                           relief='groove')
                           
        # Name entry style
        self.style.configure('Name.TEntry',
                           font=('Georgia', 12, 'bold'),
                           padding=8,
                           fieldbackground='#4a148c',
                           foreground='#ffd700',
                           borderwidth=2,
                           relief='groove')
                           
        # Mystical title style
        self.style.configure('MysticTitle.TLabel',
                           font=('Papyrus', 18, 'bold'),
                           background='#1a1a2e',
                           foreground='#ffd700')
                           
        # Oracle subtitle style
        self.style.configure('Oracle.TLabel',
                           font=('Georgia', 11, 'italic'),
                           background='#1a1a2e',
                           foreground='#e1bee7')

    def create_widgets(self):
        """Create mystical widgets"""
        # Main mystical frame
        self.main_frame = tk.Frame(self.root, bg='#1a1a2e', padx=40, pady=30)
        
        # Mystical title with crystal ball
        self.title_label = ttk.Label(
            self.main_frame, 
            text="🔮 RAMALAN NASIB PROGRAM STUDI 🔮",
            style='MysticTitle.TLabel'
        )
        
        # Oracle subtitle
        self.subtitle_label = ttk.Label(
            self.main_frame,
            text="✨ Masukkan identitas dan nilai spiritual mata pelajaranmu ✨\n🌟 Kristal ajaib akan meramal program studi terbaikmu 🌟",
            style='Oracle.TLabel',
            justify='center'
        )
        
        # Student name frame
        self.name_frame = tk.Frame(self.main_frame, bg='#16213e', 
                                  relief='ridge', bd=3, padx=25, pady=15)
        
        name_border = tk.Frame(self.name_frame, bg='#ffd700', height=2)
        name_border.pack(fill='x', pady=(0, 10))
        
        name_label = tk.Label(
            self.name_frame,
            text="👤 NAMA PENCARI TAKDIR:",
            bg='#16213e',
            fg='#ffd700',
            font=('Papyrus', 12, 'bold')
        )
        name_label.pack(pady=(0, 8))
        
        self.nama_var = tk.StringVar()
        self.nama_entry = ttk.Entry(
            self.name_frame,
            textvariable=self.nama_var,
            style='Name.TEntry',
            width=30,
            justify='center'
        )
        self.nama_entry.pack()
        
        # Mystical input frame
        self.input_frame = tk.Frame(self.main_frame, bg='#16213e', 
                                   relief='ridge', bd=4, padx=30, pady=25)
        
        # Add mystical border
        border_frame = tk.Frame(self.input_frame, bg='#4a148c', height=3)
        border_frame.pack(fill='x', pady=(0, 15))
        
        input_title = tk.Label(
            self.input_frame,
            text="📚 NILAI SPIRITUAL MATA PELAJARAN 📚",
            bg='#16213e',
            fg='#ffd700',
            font=('Papyrus', 12, 'bold')
        )
        input_title.pack(pady=(0, 15))
        
        # Subject names with mystical theme and prediction mapping
        self.subjects = {
            "🔢 Matematika Mistik": "matematika",
            "⚛️ Fisika Gaib": "fisika", 
            "🧪 Kimia Alkemis": "kimia",
            "🌿 Biologi Herbal": "biologi",
            "📜 Bahasa Nusantara": "bahasa_indonesia",
            "🗣️ Bahasa Asing": "bahasa_inggris",
            "⏳ Sejarah Kuno": "sejarah",
            "🗺️ Geografi Mistis": "geografi",
            "💰 Ekonomi Ramalan": "ekonomi",
            "👥 Sosiologi Spiritual": "sosiologi"
        }
        
        # Prediction mapping based on highest score
        self.prediction_map = {
            "biologi": "🩺 Kedokteran",
            "fisika": "⚙️ Teknik", 
            "bahasa_inggris": "🗣️ Bahasa",
            "matematika": "🔢 Matematika",
            "kimia": "🧪 Farmasi",
            "ekonomi": "💰 Ekonomi",
            "sejarah": "📜 Sejarah",
            "geografi": "🗺️ Geografi", 
            "bahasa_indonesia": "📝 Sastra Indonesia",
            "sosiologi": "👥 Ilmu Sosial"
        }
        
        self.entries = {}
        self.create_mystical_inputs()
        
        # Button frame
        self.button_frame = tk.Frame(self.main_frame, bg='#1a1a2e')
        
        # Submit button (only one button now)
        self.submit_button = ttk.Button(
            self.button_frame,
            text="🔮 RAMAL TAKDIR ANDA 🔮",
            command=self.submit_and_predict,
            style='Submit.TButton'
        )
        
        # Fortune telling area
        self.fortune_frame = tk.Frame(self.main_frame, bg='#1a1a2e')
        
        # Mystical loading label
        self.loading_label = ttk.Label(
            self.fortune_frame,
            text="",
            style='Oracle.TLabel'
        )
        
    def create_mystical_inputs(self):
        """Create mystical input fields"""
        for display_name, db_column in self.subjects.items():
            # Mystical subject frame
            subject_frame = tk.Frame(self.input_frame, bg='#16213e')
            
            # Glowing subject label
            subject_label = tk.Label(
                subject_frame,
                text=display_name,
                font=('Georgia', 10, 'bold'),
                bg='#16213e',
                fg='#e1bee7',
                width=22,
                anchor='w'
            )
            
            # Magical entry
            entry_var = tk.StringVar()
            entry = ttk.Entry(
                subject_frame,
                textvariable=entry_var,
                style='Magic.TEntry',
                width=10,
                justify='center'
            )
            
            # Add mystical validation
            entry.configure(validate='key', 
                          validatecommand=(self.root.register(self.validate_mystical_input), '%P'))
            
            # Store in mystical grimoire with db column name
            self.entries[db_column] = entry_var
            
            # Enchanted layout
            subject_label.pack(side='left', padx=(0, 15))
            entry.pack(side='right', padx=5)
            subject_frame.pack(fill='x', pady=4)
            
    def validate_mystical_input(self, value):
        """Validate mystical input"""
        if value == "":
            return True
        try:
            mystical_val = float(value)
            return 0 <= mystical_val <= 100
        except ValueError:
            return False
    
    def setup_layout(self):
        """Setup mystical layout"""
        self.main_frame.pack(fill='both', expand=True)
        
        self.title_label.pack(pady=(0, 15))
        self.subtitle_label.pack(pady=(0, 20))
        
        self.name_frame.pack(fill='x', pady=(0, 20))
        self.input_frame.pack(fill='x', pady=(0, 25))
        
        self.button_frame.pack(pady=15)
        # Center the single submit button
        self.submit_button.pack()
        
        self.fortune_frame.pack(fill='x', pady=(15, 0))
        self.loading_label.pack(fill='x')
        
    def add_mystical_effects(self):
        """Add mystical background effects"""
        self.create_floating_symbols()
        
    def create_floating_symbols(self):
        """Create floating mystical symbols"""
        symbols = ["✨", "🌟", "⭐", "💫", "🔮", "🌙", "⚡"]
        
        def animate_symbol():
            symbol = random.choice(symbols)
            x = random.randint(50, 750)
            y = random.randint(100, 900)
            
            symbol_label = tk.Label(
                self.root, 
                text=symbol, 
                bg='#1a1a2e', 
                fg='#ffd700',
                font=('Arial', random.randint(12, 18))
            )
            symbol_label.place(x=x, y=y)
            
            # Animate floating
            def float_up(current_y, alpha=1.0):
                if current_y > -50 and alpha > 0:
                    symbol_label.place(y=current_y - 2)
                    self.root.after(100, lambda: float_up(current_y - 2, alpha - 0.02))
                else:
                    symbol_label.destroy()
            
            float_up(y)
            
        # Schedule next symbol
        self.root.after(random.randint(3000, 6000), animate_symbol)
        animate_symbol()
    
    def get_prediction_based_on_highest(self):
        """Get prediction based on highest score with special logic for Technology Information"""
        scores = {}
        
        # Collect all non-empty scores
        for db_column, entry_var in self.entries.items():
            value = entry_var.get().strip()
            if value:
                try:
                    scores[db_column] = float(value)
                except ValueError:
                    continue
        
        if not scores:
            return "🎯 Teknologi Informasi"  # Default
        
        # Special logic for Technology Information
        # If both Math and Physics scores are >= 80, prioritize Technology Information
        if ("matematika" in scores and "fisika" in scores and 
            scores["matematika"] >= 80 and scores["fisika"] >= 80):
            avg_math_physics = (scores["matematika"] + scores["fisika"]) / 2
            return "🎯 Teknologi Informasi", "matematika_fisika", avg_math_physics
        
        # Alternative: If Math or Physics is highest AND >= 75, consider Technology Information
        highest_subject = max(scores, key=scores.get)
        highest_score = scores[highest_subject]
        
        if ((highest_subject == "matematika" or highest_subject == "fisika") and 
            highest_score >= 75):
            # Check if the other subject (math or physics) also has decent score
            other_subject = "fisika" if highest_subject == "matematika" else "matematika"
            if other_subject in scores and scores[other_subject] >= 70:
                combined_score = (highest_score + scores[other_subject]) / 2
                return "🎯 Teknologi Informasi", f"{highest_subject}_{other_subject}", combined_score
        
        # Get prediction from regular mapping
        prediction = self.prediction_map.get(highest_subject, "🎯 Teknologi Informasi")
        
        return prediction, highest_subject, highest_score
    
    def submit_and_predict(self):
        """Submit data to database and predict with enhanced validation"""
        # Validate name first
        nama = self.nama_var.get().strip()
        if not nama:
            self.show_mystical_warning("⚠️ NAMA ANDA TIDAK BOLEH KOSONG! ⚠️\n\n🔮 Masukkan nama pencari takdir\nagar kristal dapat mengenali identitasmu\n\n✨ Tanpa identitas, ramalan tak dapat dimulai ✨")
            return
        
        # Check and validate input values
        filled_fields = 0
        invalid_values = []
        
        for display_name, db_column in self.subjects.items():
            value = self.entries[db_column].get().strip()
            if value:
                try:
                    float_val = float(value)
                    if not (0 <= float_val <= 100):
                        invalid_values.append(f"{display_name}: {value}")
                    else:
                        filled_fields += 1
                except ValueError:
                    invalid_values.append(f"{display_name}: {value}")
        
        # Show error if there are invalid values
        if invalid_values:
            error_message = "⚠️ NILAI HARUS BERUPA ANGKA 0-100! ⚠️\n\n🔮 Nilai yang tidak valid:\n"
            for invalid in invalid_values[:3]:  # Show max 3 errors
                error_message += f"• {invalid}\n"
            if len(invalid_values) > 3:
                error_message += f"• ... dan {len(invalid_values) - 3} lainnya\n"
            error_message += "\n✨ Masukkan angka 0-100 untuk semua nilai! ✨"
            
            self.show_mystical_warning(error_message)
            return
        
        # Check if at least some fields are filled
        if filled_fields == 0:
            self.show_mystical_warning("⚠️ ENERGI SPIRITUAL KURANG! ⚠️\n\n🔮 Masukkan setidaknya satu nilai\nagar kristal dapat meramal nasibmu\n\n✨ Tanpa energi, ramalan tak dapat dimulai ✨")
            return
        
        # Get prediction and save to database
        self.save_to_database_and_predict(nama)
    
    def save_to_database_and_predict(self, nama):
        """Save data to database and show prediction"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Prepare data
            values = {}
            total = 0
            count = 0
            
            for db_column, entry_var in self.entries.items():
                value = entry_var.get().strip()
                if value:
                    try:
                        float_val = float(value)
                        values[db_column] = float_val
                        total += float_val
                        count += 1
                    except ValueError:
                        values[db_column] = None
                else:
                    values[db_column] = None
            
            # Calculate average
            rata_rata = total / count if count > 0 else 0
            
            # Get prediction
            if count > 0:
                prediction_result = self.get_prediction_based_on_highest()
                if isinstance(prediction_result, tuple):
                    prediksi, highest_subject, highest_score = prediction_result
                else:
                    prediksi = prediction_result
                    highest_subject = "teknologi_informasi"
                    highest_score = rata_rata
            else:
                prediksi = "🎯 Teknologi Informasi"
                highest_subject = "teknologi_informasi"
                highest_score = 0
            
            # Insert into database
            cursor.execute('''
                INSERT INTO crystal_ball
                (nama_peramal, matematika, fisika, kimia, biologi, bahasa_indonesia, 
                 bahasa_inggris, sejarah, geografi, ekonomi, sosiologi, 
                 prediksi_fakultas, rata_rata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                nama,
                values.get('matematika'),
                values.get('fisika'), 
                values.get('kimia'),
                values.get('biologi'),
                values.get('bahasa_indonesia'),
                values.get('bahasa_inggris'),
                values.get('sejarah'),
                values.get('geografi'),
                values.get('ekonomi'),
                values.get('sosiologi'),
                prediksi,
                rata_rata
            ))
            
            conn.commit()
            conn.close()
            
            # Show success message and prediction
            self.mystical_loading_ritual(nama=nama, prediksi=prediksi, 
                                       rata_rata=rata_rata, count=count, 
                                       highest_subject=highest_subject, highest_score=highest_score)
            
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan data: {str(e)}")
    
    def show_mystical_warning(self, message):
        """Show mystical warning"""
        warning_window = tk.Toplevel(self.root)
        warning_window.title("🔮 Peringatan Spiritual")
        warning_window.geometry("450x300")
        warning_window.configure(bg='#4a148c')
        warning_window.transient(self.root)
        warning_window.grab_set()
        
        # Center warning
        warning_window.update_idletasks()
        x = (warning_window.winfo_screenwidth() // 2) - (450 // 2)
        y = (warning_window.winfo_screenheight() // 2) - (300 // 2)
        warning_window.geometry(f"450x300+{x}+{y}")
        
        # Warning symbol
        warning_symbol = tk.Label(
            warning_window,
            text="⚠️",
            bg='#4a148c',
            fg='#ff6b6b',
            font=('Arial', 50)
        )
        warning_symbol.pack(pady=(20, 10))
        
        warning_label = tk.Label(
            warning_window,
            text=message,
            bg='#4a148c',
            fg='#ffd700',
            font=('Georgia', 11, 'bold'),
            justify='center',
            wraplength=400
        )
        warning_label.pack(expand=True, padx=20)
        
        ok_button = tk.Button(
            warning_window,
            text="🙏 SAYA MENGERTI",
            bg='#ffd700',
            fg='#4a148c',
            font=('Papyrus', 12, 'bold'),
            command=warning_window.destroy,
            padx=30,
            pady=10,
            relief='raised',
            bd=3
        )
        ok_button.pack(pady=20)
    
    def mystical_loading_ritual(self, **kwargs):
        """Perform mystical loading ritual"""
        ritual_texts = [
            "💾 Menyimpan data ke grimoire digital...",
            "🔮 Menganalisis pola spiritual...",
            "✨ Mengaktifkan kristal prediksi...",
            "🌟 Membaca takdir dari bola kristal mystis...",
            "⚡ Menghubungkan dengan mata batin...",
            "💫 Mengungkap rahasia masa depan..."
        ]
        
        def ritual_animation(index=0, dot_count=0):
            if index < len(ritual_texts):
                dots = "." * (dot_count % 4)
                text = ritual_texts[index] + dots
                self.loading_label.configure(text=text)
                
                if dot_count < 6:
                    self.root.after(300, lambda: ritual_animation(index, dot_count + 1))
                else:
                    self.root.after(500, lambda: ritual_animation(index + 1, 0))
            else:
                self.root.after(1000, lambda: self.reveal_saved_destiny(**kwargs))
        
        ritual_animation()
    
    def reveal_saved_destiny(self, nama, prediksi, rata_rata, count, highest_subject, highest_score):
        """Reveal saved destiny"""
        self.loading_label.configure(text="")
        self.create_mystical_popup(rata_rata, count, prediksi, saved=True, nama=nama,
                                 highest_subject=highest_subject, highest_score=highest_score)
    
    def create_mystical_popup(self, average, count, prediction, saved=False, nama="", 
                            highest_subject="", highest_score=0):
        """Create beautiful mystical popup like sweet alert"""
        popup = tk.Toplevel(self.root)
        popup.title("🔮 Ramalan Takdir Terungkap")
        popup.geometry("550x700")
        popup.configure(bg='#1a1a2e')
        popup.transient(self.root)
        popup.grab_set()
        popup.resizable(False, False)
        
        # Center popup
        popup.update_idletasks()
        x = (popup.winfo_screenwidth() // 2) - (550 // 2)
        y = (popup.winfo_screenheight() // 2) - (700 // 2)
        popup.geometry(f"550x700+{x}+{y}")
        
        # Mystical border
        border_frame = tk.Frame(popup, bg='#ffd700', height=5)
        border_frame.pack(fill='x')
        
        # Main content frame
        content_frame = tk.Frame(popup, bg='#1a1a2e', padx=30, pady=30)
        content_frame.pack(fill='both', expand=True)
        
        # Animated crystal ball
        crystal_label = tk.Label(
            content_frame,
            text="🔮",
            bg='#1a1a2e',
            fg='#ffd700',
            font=('Arial', 60)
        )
        crystal_label.pack(pady=(0, 20))
        
        # Destiny revealed title
        title_text = "💾 TAKDIR MU TERUNGKAP! ✨"
            
        title_label = tk.Label(
            content_frame,
            text=title_text,
            bg='#1a1a2e',
            fg='#ffd700',
            font=('Papyrus', 16, 'bold')
        )
        title_label.pack(pady=(0, 15))
        
        # Name display
        if nama:
            name_label = tk.Label(
                content_frame,
                text=f"👤 Pencari Takdir: {nama}",
                bg='#1a1a2e',
                fg='#e1bee7',
                font=('Georgia', 12, 'bold')
            )
            name_label.pack(pady=(0, 10))
        
        # Mystical result frame
        result_frame = tk.Frame(content_frame, bg='#4a148c', relief='raised', bd=3, padx=20, pady=20)
        result_frame.pack(fill='x', pady=(0, 20))
        
        # Main prediction
        prediction_label = tk.Label(
            result_frame,
            text=f"🎯 PROGRAM STUDI TAKDIR MU:\n\n{prediction}",
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 16, 'bold'),
            justify='center'
        )
        prediction_label.pack()
        
        # Mystical details
        details_text = f"🌟 Energi Spiritual Rata-rata: {average:.1f}/100\n"
        details_text += f"📊 Mata Pelajaran Teraktivasi: {count}/10\n"
        if highest_subject and highest_score > 0:
            subject_display = {
                'biologi': 'Biologi Herbal', 'fisika': 'Fisika Gaib', 'bahasa_inggris': 'Bahasa Asing',
                'matematika': 'Matematika Mistik', 'kimia': 'Kimia Alkemis', 'ekonomi': 'Ekonomi Ramalan',
                'sejarah': 'Sejarah Kuno', 'geografi': 'Geografi Mistis', 
                'bahasa_indonesia': 'Bahasa Nusantara', 'sosiologi': 'Sosiologi Spiritual',
                'matematika_fisika': 'Kombinasi Matematika & Fisika Mistik',
                'matematika_fisika': 'Matematika & Fisika Gaib',
                'fisika_matematika': 'Fisika & Matematika Mistik'
            }
            details_text += f"🏆 Kekuatan Tertinggi: {subject_display.get(highest_subject, highest_subject)} ({highest_score:.1f})\n"
        details_text += f"🔮 Tingkat Kepercayaan: 99.9%\n\n"
        details_text += "💫 RAMALAN MATA BATIN:\n"
        
        # Special oracle message for Technology Information
        if prediction == "🎯 Teknologi Informasi":
            details_text += '"Kristal digital berkilauan! Energi matematika\n'
            details_text += 'dan fisika bergabung dalam harmoni teknologi.\n'
            details_text += 'Masa depanmu terukir dalam kode dan algoritma!"'
        else:
            details_text += '"Bintang-bintang berbisik tentang masa\n'
            details_text += 'depanmu di bidang yang kau kuasai.\n'
            details_text += 'Ikuti passion dan raih takdir gemilangmu!"'
        
        details_text += f"\n\n💾 Takdir telah tersimpan dalam bola kristal mystis"
        
        details_label = tk.Label(
            content_frame,
            text=details_text,
            bg='#1a1a2e',
            fg='#e1bee7',
            font=('Georgia', 10),
            justify='center'
        )
        details_label.pack(pady=(0, 20))
        
        # Action buttons frame
        button_frame = tk.Frame(content_frame, bg='#1a1a2e')
        button_frame.pack(fill='x')
        
        # Accept destiny button
        accept_button = tk.Button(
            button_frame,
            text="🙏 TERIMA TAKDIR",
            bg='#ffd700',
            fg='#4a148c',
            font=('Papyrus', 12, 'bold'),
            command=popup.destroy,
            padx=20,
            pady=8,
            relief='raised',
            bd=2
        )
        accept_button.pack(side='left', padx=(0, 10), expand=True, fill='x')
        
        # Ramal again button
        again_button = tk.Button(
            button_frame,
            text="🔮 RAMAL LAGI",
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 12, 'bold'),
            command=lambda: [popup.destroy(), self.clear_mystical_inputs()],
            padx=20,
            pady=8,
            relief='raised',
            bd=2
        )
        again_button.pack(side='right', expand=True, fill='x')
        
        # Add sparkle animation to crystal ball
        self.animate_crystal(crystal_label)
        
        # Play mystical sound effect (visual representation)
        self.mystical_sound_effect(popup)
    
    def animate_crystal(self, crystal_label):
        """Animate the crystal ball"""
        crystals = ["🔮", "💎", "🌟", "✨"]
        current = 0
        
        def rotate_crystal():
            nonlocal current
            crystal_label.configure(text=crystals[current % len(crystals)])
            current += 1
            crystal_label.after(500, rotate_crystal)
        
        rotate_crystal()
    
    def mystical_sound_effect(self, popup):
        """Visual sound effect"""
        sound_frame = tk.Frame(popup, bg='#1a1a2e')
        sound_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        sound_label = tk.Label(
            sound_frame,
            text="🎵 ♪ ♫ ♪ ♫ ♪ 🎵",
            bg='#1a1a2e',
            fg='#ffd700',
            font=('Arial', 14)
        )
        sound_label.pack(expand=True)
        
        def fade_sound():
            sound_frame.destroy()
        
        popup.after(2000, fade_sound)
    
    def clear_mystical_inputs(self):
        """Clear all mystical inputs"""
        self.nama_var.set("")
        for entry_var in self.entries.values():
            entry_var.set("")
    
    def view_database(self):
        """View saved data from database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT nama_peramal, prediksi_fakultas, rata_rata, tanggal_input 
                FROM crystal_ball 
                ORDER BY tanggal_input DESC LIMIT 10
            ''')
            
            records = cursor.fetchall()
            conn.close()
            
            if not records:
                messagebox.showinfo("Bola Kristal Mystis", "🔮 Belum ada Ramalan Takdir dalam grimoire digital")
                return
            
            # Create database view window
            db_window = tk.Toplevel(self.root)
            db_window.title("📚 Grimoire Digital - Riwayat Ramalan")
            db_window.geometry("600x400")
            db_window.configure(bg='#1a1a2e')
            db_window.transient(self.root)
            
            # Center window
            db_window.update_idletasks()
            x = (db_window.winfo_screenwidth() // 2) - (600 // 2)
            y = (db_window.winfo_screenheight() // 2) - (400 // 2)
            db_window.geometry(f"600x400+{x}+{y}")
            
            # Title
            title_label = tk.Label(
                db_window,
                text="📚 GRIMOIRE DIGITAL 📚\nRiwayat 10 Ramalan Terakhir",
                bg='#1a1a2e',
                fg='#ffd700',
                font=('Papyrus', 14, 'bold'),
                justify='center'
            )
            title_label.pack(pady=20)
            
            # Create treeview for data display
            tree_frame = tk.Frame(db_window, bg='#1a1a2e')
            tree_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
            
            # Treeview with scrollbar
            tree = ttk.Treeview(tree_frame, columns=('Nama', 'Prediksi', 'Rata-rata', 'Tanggal'), 
                               show='headings', height=12)
            
            # Define headings
            tree.heading('Nama', text='👤 Nama')
            tree.heading('Prediksi', text='🎯 Prediksi')
            tree.heading('Rata-rata', text='📊 Rata-rata')
            tree.heading('Tanggal', text='📅 Tanggal')
            
            # Configure columns
            tree.column('Nama', width=150, anchor='center')
            tree.column('Prediksi', width=200, anchor='center')
            tree.column('Rata-rata', width=100, anchor='center')
            tree.column('Tanggal', width=130, anchor='center')
            
            # Add scrollbar
            scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            # Insert data
            for record in records:
                nama, prediksi, rata_rata, tanggal = record
                tanggal_format = tanggal.split(' ')[0] if tanggal else "N/A"
                tree.insert('', 'end', values=(nama, prediksi, f"{rata_rata:.1f}", tanggal_format))
            
            # Pack treeview and scrollbar
            tree.pack(side='left', fill='both', expand=True)
            scrollbar.pack(side='right', fill='y')
            
            # Close button
            close_button = tk.Button(
                db_window,
                text="🚪 TUTUP GRIMOIRE",
                bg='#4a148c',
                fg='#ffd700',
                font=('Papyrus', 10, 'bold'),
                command=db_window.destroy,
                pady=5
            )
            close_button.pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat membaca bola kristal: {str(e)}")

def main():
    """Summon the mystical application"""
    root = tk.Tk()
    app = MysticProdiApp(root)
    
    # Add menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # Database menu
    db_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="📚 Grimoire", menu=db_menu)
    db_menu.add_command(label="📖 Lihat Riwayat Ramalan", command=app.view_database)
    db_menu.add_separator()
    db_menu.add_command(label="🚪 Keluar", command=root.quit)
    
    # Mystical shortcuts
    root.bind('<Return>', lambda e: app.submit_button.invoke())
    root.bind('<Control-q>', lambda e: root.quit())
    root.bind('<Escape>', lambda e: root.quit())
    root.bind('<F1>', lambda e: app.view_database())
    
    # Mystical welcome
    def show_mystical_welcome():
        welcome = tk.Toplevel(root)
        welcome.title("🔮 Selamat Datang ke Dunia Mistis")
        welcome.geometry("500x350")
        welcome.configure(bg='#4a148c')
        welcome.transient(root)
        welcome.grab_set()
        
        # Center welcome
        welcome.update_idletasks()
        x = (welcome.winfo_screenwidth() // 2) - (500 // 2)
        y = (welcome.winfo_screenheight() // 2) - (350 // 2)
        welcome.geometry(f"500x350+{x}+{y}")
        
        welcome_text = """🔮 SELAMAT DATANG, PENCARI TAKDIR! 🔮

✨ Aplikasi ramalan ini akan mengungkap
program studi yang ditakdirkan untukmu ✨

🌟 FITUR APLIKASI:
• 💾 Simpan data ke database SQLite
• 🎯 Prediksi berdasarkan nilai tertinggi
• 📚 Lihat riwayat ramalan (F1)
• ⚠️ Validasi input yang ketat
• 🔮 Satu tombol untuk ramal dan simpan
• 💻 Logika khusus Teknologi Informasi

🌟 PANDUAN MYSTIS:
• Masukkan nama dan nilai spiritual (0-100)
• Nilai harus berupa angka antara 0-100
• Tekan "🔮 RAMAL TAKDIR ANDA 🔮" untuk prediksi
• ESC untuk meninggalkan dunia mistis

💻 RAHASIA TEKNOLOGI INFORMASI:
• Matematika ≥80 DAN Fisika ≥80 = TI
• Matematika/Fisika tertinggi ≥75 + yang lain ≥70 = TI

🔥 Bersiaplah untuk menyaksikan keajaiban! 🔥"""
        
        label = tk.Label(
            welcome,
            text=welcome_text,
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 10, 'bold'),
            justify='center'
        )
        label.pack(expand=True, padx=20)
        
        ok_btn = tk.Button(
            welcome,
            text="🚀 MULAI PERJALANAN MISTIS!",
            bg='#ffd700',
            fg='#4a148c',
            font=('Papyrus', 10, 'bold'),
            command=welcome.destroy,
            pady=5
        )
        ok_btn.pack(pady=15)
    
    root.after(800, show_mystical_welcome)
    root.mainloop()

if __name__ == "__main__":
    main()