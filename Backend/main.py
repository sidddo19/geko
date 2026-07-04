from fastapi import FastAPI
from crawler import crawl_website
from ai import analyze_company
from pdf_generator import generate_pdf
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Geko AI is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/crawl")
def crawl(url: str):
    data = crawl_website(url)
    return data

@app.get("/research")
def research(url: str):
    print("STEP 1: Crawling website...")

    data = crawl_website(url)

    print("STEP 2: Crawl finished")

    if "error" in data:
        return data

    print("Text length:", len(data["text"]))

    print("STEP 3: Sending to Gemini")

    ai_result = analyze_company(data["text"])

    print("STEP 4: Gemini finished")

    return {
        "url": url,
        "analysis": ai_result
    }

@app.get("/download-report")
def download_report(url: str):
    data = crawl_website(url)

    if "error" in data:
        return data

    ai_result = analyze_company(data["text"])

    file_path = generate_pdf(url, ai_result)

    return FileResponse(
        path=file_path,
        filename="Geko_AI_Report.pdf",
        media_type="application/pdf"
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)