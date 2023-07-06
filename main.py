import tkinter as tk
from tkinter import ttk
import customtkinter as cctk
from PIL import Image, ImageTk


class BookSearchApp:
    def __init__(self):
        cctk.set_appearance_mode('light')
        self.books = {
            "کتاب هزار پیشه": {"content": "کتاب هزار پیشه، رمانی نوشته ی چارلز بوکفسکی است که اولین بار در سال 1975 منتشر شد. داستان این رمان عجیب، جذاب و به یاد ماندنی به سرگردانی ها و دغدغه های نویسنده ای به نام هنری چیناسکی در آمریکای درگیر در جنگ جهانی دوم می پردازد. چیناسکی که از خدمت سربازی معاف شده، از شهری به شهر دیگر و از شغلی به شغل دیگر می رود و همیشه نیازمند پول است اما نه آنقدرها که مجبور شود به هر قیمتی شغل خود را نگه دارد. زندگی روتین این شخصیت را فاحشه ها، اتاق های نمور، افسردگی های گاه و بیگاه و دعواهای ناشی از مستی شکل داده است. رمان هزار پیشه، تصویری شفاف و هنرمندانه از زندگی در پایین ترین سطوح اجتماع و اعتیاد به الکل است و به خوبی می تواند کتاب‌دوستان را با دنیای تخیلات عجیب بوکفسکی آشنا کند.", "image_path": "book1.jpg"},
            "کتاب هالیوود": {"content": "نقد و بررسی  معرفی کتاب هالیوود  کتاب هالیوود، رمانی نوشته ی چارلز بوکفسکی است که اولین بار در سال 1989 منتشر شد. هنری چیناسکی، خویشتنِ داستانی بوکفسکی، تحت فشار قرار می گیرد تا کتابی نیمه خودزندگی نامه ای را به یک فیلمنامه تبدیل کند. او با اکراه این مسئولیت را می پذیرد و پا به دنیایی عجیب و ناآشنا به نام هالیوود می گذارد. کتاب های جنجال برانگیز زیادی درباره ی زندگی در هالیوود وجود دارند اما هیچ کدام به اندازه ی این رمان، شاعرانه و مخاطره آمیز نیستند. کتاب هالیوود را می توان شرحی داستانی از تجارب بوکفسکی در نوشتن فیلمنامه در نظر گرفت. چیناسکی در طول سفر پرفراز و نشیبِ تبدیل از یک شاعر به یک فیلمنامه نویس، با تعدادی از ستاره های شناخته شده ی سینما رو به رو می شود و از پوچی و خودشیفتگی های برخی افراد فعال در صنعت فیلمسازی پرده برمی دارد. ", "image_path": "book2.jpg"},#
            "کتاب حل مسائل #C": {"content": "کتاب حل مسائل #C اثر رمضان عباس نژاد ورزی، با بهره‌گیری از سال‌ها تجربه در زمینه تدریس، تالیف، برنامه‌نویسی و مدیریت پروژه‌های نرم‌افزاری تدوین شده است. از ویژگی‌های بارز این کتاب، بیان مثال‌های کاربردی و حل گام‌به‌گام به همراه توضیحات دقیق آن‌ها است.  زبان #C در فناوری‌ دات‌نت (NET.) توسط شرکت مایکروسافت ارائه شده است که کاملاً شئ‌گرا است. امروزه، اکثر دانشجویان رشته کامپیوتر و فناوری اطلاعات با این زبان آشنایی دارند. زیرا، این زبان از محبوب‌ترین زبان‌های خانواده C می‌باشد. از طرف دیگر، زبان #C به عنوان یکی از مهم‌ترین زبان‌های رشته کامپیوتر، فناوری اطلاعات، ICT، علوم‌ کامپیوتر و رشته‌های دیگر تحت عنوان درس زبان برنامه‌نویسی پیشرفته تدریس می‌شود. یکی از روش‌های موفق یادگیری زبان‌های برنامه‌نویسی، حل مسائل گوناگون می‌باشد.  مثال‌هایی که در کتاب حل مسائل #C (مرجع کامل) آورده شده‌اند، همگی دارای کاربرد و هدف خاصی در برنامه‌نویسی هستند و برخی از آن‌ها را می‌توانید در پروژه‌های کاربردی و بزرگ استفاده کنید. در این کتاب حدود 180 مثال برنامه‌نویسی و حل 8 پروژه برنامه‌نویسی آمده است.", "image_path": "book3.jpg"}
        }

        self.root = cctk.CTk()
        self.root.title("Book Search App")
        self.root.geometry('500x600')
        self.root.resizable(width=False, height=False)

        self.search_frame = cctk.CTkFrame(self.root)
        self.search_frame.pack(padx=12,pady=10,anchor='e')

        self.search_entry = cctk.CTkEntry(self.search_frame, corner_radius=0, width=300, font=('roboto', 15))
        self.search_entry.pack(anchor='e', side='left')

        self.search_button = cctk.CTkButton(self.search_frame, text="Search", command=self.search_books, width=20, corner_radius=0, font=('bold', 15))
        self.search_button.pack(anchor='e')

        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack()

        self.content_text = tk.Text(self.root, height=100, width=100, font=('roboto', 15))
        self.content_text.pack()

    def search_books(self):
        search_query = self.search_entry.get().lower()
        self.clear_results()

        for book, data in self.books.items():
            if search_query in book.lower():
                content = data["content"]
                image_path = data["image_path"]
                image = ImageTk.PhotoImage(Image.open(image_path).resize((128, 128 )))
                book_button = ttk.Button(self.result_frame, text=book, image=image, compound=tk.TOP, command=lambda content=content: self.show_content(content))
                book_button.image = image  
                book_button.pack(side=tk.LEFT)

    def show_content(self, content):
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert(tk.END, content)

    def clear_results(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

app = BookSearchApp()
app.run()
