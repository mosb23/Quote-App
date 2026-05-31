from pathlib import Path

from pypdf import PdfReader


pdf_path = Path("submission/Quote_App_Submission_Mohamed_Ahmed_Abouelenein.pdf")
reader = PdfReader(str(pdf_path))
text = "\n".join((page.extract_text() or "") for page in reader.pages)

image_count = 0
for page in reader.pages:
    resources = page.get("/Resources") or {}
    xobjects = resources.get("/XObject") or {}
    for obj in xobjects.values():
        try:
            if obj.get_object().get("/Subtype") == "/Image":
                image_count += 1
        except Exception:
            pass

checks = {
    "pages": len(reader.pages),
    "has_name": "Mohamed Ahmed Abouelenein" in text,
    "has_id": "211006095" in text,
    "has_email": "mohameed.ahmedd077@gmail.com" in text,
    "has_phone": "+201028239305" in text,
    "has_repo": "https://github.com/mosb23/Quote-App" in text,
    "has_code": "class QuoteApp extends StatelessWidget" in text
    and "void showNextQuote()" in text,
    "images": image_count,
}

for key, value in checks.items():
    print(f"{key}: {value}")
