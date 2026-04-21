import os
import jinja2

class ReportGenerator:
    def __init__(self, template_dir, output_dir):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.template_dir))

    def generate_report(self, data, template_name):
        template = self.jinja_env.get_template(template_name)
        output_file = os.path.join(self.output_dir, f"{template_name}.txt")
        with open(output_file, "w") as f:
            f.write(template.render(data))

# Misol foydalanish
if __name__ == "__main__":
    report_generator = ReportGenerator("templates", "output")
    data = {"name": "John", "age": 30}
    report_generator.generate_report(data, "example")
```

```bash
# templates dizini ichida example.html fayli mavjud bo'lishi kerak
# example.html faylini quyidagicha yozing:
# <h1>{{ name }}, {{ age }} yoshda</h1>

# output dizini yaratib, report_generator.py skriptini ishga tushiring
# Natija output dizinida example.txt fayli bo'lishi kerak
```

```bash
# output dizini ichida example.txt faylini quyidagicha ko'ring:
# <h1>John, 30 yoshda</h1>
