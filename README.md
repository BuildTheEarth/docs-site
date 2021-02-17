# bteguide-site
Source for the BTE ReadTheDocs. Exclusively contains configuration and custom code that doesn't belong in the actual documentation.

## Contributing to Development

Install the required packages with:
```
 $ pip install -r requirements.txt
```

The Makefile and make.bat are both configured with Live Reload enabled. Start the live server with:

**Windows**
```
 $ .\make.bat livehtml
```
**Linux/macOS**
```
 $ make livehtml
```

## Fetching/Updating the source documents

Fetching the source for the actual site:
```
 $ git submodule init
 $ git submodule update
```

Updating the source to push an update:
```
 $ git submodule update --remote
```
Make sure you trigger a build via the RTFD Project Home.