{
    "targets": [{
        "target_name": "fstream-addon",
        "sources": [
            "main.cc",
        ],
        'include_dirs': [
            "<!@(node -p \"require('node-addon-api').include\")"
        ],
        'libraries': [],
        'dependencies': [
            "<!(node -p \"require('node-addon-api').gyp\")"
        ],
      "configurations": {
        "Release": {
	  "msvs_settings": {
            "VCCLCompilerTool": {
    	      "RuntimeTypeInfo": "true",
	      "RuntimeLibrary" : 2,
	       "AdditionalOptions": ["/EHsc"],
            },
          }
        }
      },
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
           }]
}
