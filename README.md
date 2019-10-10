# piscripts

Some Scripts for the Raspberry PI

# Convert images for InkHat

convert keystrokes.png -define png:bit-depth=8 -define png:color-type=3 keystrokes_bw.png


# Would like to:
	- Detect connection and disconection from network. For example, to upload pending data on connection
        - Take pictures and video
        - Detect level of battery
        - control Inky hat (converting images automatically for compatibility)
        - control display UI? Terminal UI ?
        - Have websockets connect to a remote service for messaging
        - Create and manage: Media collection, Time series
        - Have a timer event  
        - all with asyncio
        - Monitor bluetooth 
        - Detect faces
        - Monitor screen connection and disconnection
