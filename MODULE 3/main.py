from fastapi import FASTAPI
app = FASTAPI(
    title="Pincode look up feature Api ",
    description="this api auto fill the pincode and city name based on the pincode entered by the user",
    version="1.0.0",)

@app.get("/")
async def root():
    return {"message": "Pincode Lookup API"}
