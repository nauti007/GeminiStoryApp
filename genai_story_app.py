import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QTextEdit, QPushButton, QLabel)
from google import genai
from google.genai import types
try:
    import config
    client = genai.Client(api_key=config.api_key)
except Exception as e:
    print(f"Error: Make sure config.py exists. {e}")

class GeminiStoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Story Generator")
        self.setGeometry(100, 100, 600, 500)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Enter a Story Topic:")
        layout.addWidget(self.label)
        
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("e.g., A robot finding a garden...")
        layout.addWidget(self.input_box)
        
        self.btn = QPushButton("Generate with Gemini 2.5 Flash")
        self.btn.clicked.connect(self.run_generation)
        layout.addWidget(self.btn)
        
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)
        
        self.setLayout(layout)

    def run_generation(self):
        topic = self.input_box.toPlainText()
        if not topic.strip():
            self.output_box.setText("Please enter a topic first!")
            return
            
        self.output_box.setText("Generating story... please wait.")
        
        # Use your proven stable logic
        result = self.generate_text_logic(topic)
        self.output_box.setText(result)

    def generate_text_logic(self, prompt):
        model_id = "gemini-2.5-flash"
        config_settings = types.GenerateContentConfig(
            max_output_tokens=300,
            temperature=1.0,
            top_p=0.95,
            top_k=40
        )

        try:
            formatted_prompt = f"TASK: Write a 3-sentence story.\nTOPIC: {prompt}\nSTORY:"
            response = client.models.generate_content(
                model=model_id,
                contents=[formatted_prompt],
                config=config_settings
            )
            return response.text.strip() if response.text else "[Empty Response]"
        except Exception as e:
            return f"[API Error: {str(e)}]"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GeminiStoryApp()
    ex.show()
    sys.exit(app.exec())