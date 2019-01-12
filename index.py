from app import io

def main():
    ios = io.IOStreams()
    inputFileName = "text-big.txt"
    positions = ios.getBlockIntervalPositions( inputFileName )
    ios.getContentFileByInterval( inputFileName, positions, len(positions) )

main()