import asyncio
import sys
import edge_tts

async def main():
    if len(sys.argv) < 4:
        print("Usage: tts_generator.py <text> <voice> <output_path>")
        sys.exit(1)
        
    text = sys.argv[1]
    voice = sys.argv[2]
    output_path = sys.argv[3]
    
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

if __name__ == "__main__":
    asyncio.run(main())
