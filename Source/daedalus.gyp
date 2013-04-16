 {
    'targets': [
      {
        'target_name': 'daedalus',
        'type': 'executable',
        'xcode_settings': {
          'OTHER_CFLAGS': [
            '-Werror',
            '-Wformat=0',
            #'-O4',
            #'-g'
          ],
        },
        'dependencies': [
          'SysGL/SysGL.gyp:SysGL',
          'third_party/glfw/glfw.gyp:glfw', # FIXME: should transitively pull in include dir
          'third_party/libpng/libpng.gyp:libpng',
          'third_party/webby/webby.gyp:webby',
          'third_party/zlib/zlib.gyp:minizip',
          'third_party/zlib/zlib.gyp:zlib',
        ],
        'include_dirs': [
          '.',
          'Config/Dev',
        ],
        'defines': [
          'DAEDALUS_ACCURATE_TMEM',
        ],
        'sources': [
          'Core/Cheats.cpp',
          'Core/CPU.cpp',
          'Core/DMA.cpp',
          'Core/Dynamo.cpp',
          'Core/FlashMem.cpp',
          'Core/Interpret.cpp',
          'Core/Interrupts.cpp',
          'Core/JpegTask.cpp',
          'Core/Memory.cpp',
          'Core/PIF.cpp',
          'Core/R4300.cpp',
          'Core/Registers.cpp',
          'Core/ROM.cpp',
          'Core/ROMBuffer.cpp',
          'Core/ROMImage.cpp',
          'Core/RomSettings.cpp',
          'Core/RSP_HLE.cpp',
          'Core/Save.cpp',
          'Core/SaveState.cpp',
          'Core/TLB.cpp',
          'Debug/DebugConsoleImpl.cpp',
          'Debug/DebugLog.cpp',
          'Debug/Dump.cpp',
          'DynaRec/BranchType.cpp',
          'DynaRec/Fragment.cpp',
          'DynaRec/FragmentCache.cpp',
          'DynaRec/IndirectExitMap.cpp',
          'DynaRec/StaticAnalysis.cpp',
          'DynaRec/TraceRecorder.cpp',
          'Graphics/ColourValue.cpp',
          'Graphics/PngUtil.cpp',
          'Graphics/TextureTransform.cpp',
          'HLEAudio/ABI1.cpp',
          'HLEAudio/ABI2.cpp',
          'HLEAudio/ABI3.cpp',
          'HLEAudio/ABI3mp3.cpp',
          'HLEAudio/AudioBuffer.cpp',
          'HLEAudio/AudioHLEProcessor.cpp',
          'HLEAudio/HLEMain.cpp',
          'HLEGraphics/BaseRenderer.cpp',
          'HLEGraphics/CachedTexture.cpp',
          'HLEGraphics/ConvertImage.cpp',
          'HLEGraphics/ConvertTile.cpp',
          'HLEGraphics/DLDebug.cpp',
          'HLEGraphics/DLParser.cpp',
          'HLEGraphics/Microcode.cpp',
          'HLEGraphics/RDP.cpp',
          'HLEGraphics/RDPStateManager.cpp',
          'HLEGraphics/TextureCache.cpp',
          'HLEGraphics/TextureCacheWebDebug.cpp',
          'HLEGraphics/TextureInfo.cpp',
          'HLEGraphics/uCodes/Ucode.cpp',
          'Interface/RomDB.cpp',
          'Math/Matrix4x4.cpp',
          'Plugins/GraphicsPlugin.cpp',
          'Test/BatchTest.cpp',
          'Utility/CRC.cpp',
          'Utility/DataSink.cpp',
          'Utility/FastMemcpy.cpp',
          'Utility/FramerateLimiter.cpp',
          'Utility/Hash.cpp',
          'Utility/IniFile.cpp',
          'Utility/MemoryHeap.cpp',
          'Utility/Preferences.cpp',
          'Utility/PrintOpCode.cpp',
          'Utility/ROMFile.cpp',
          'Utility/ROMFileCache.cpp',
          'Utility/ROMFileCompressed.cpp',
          'Utility/ROMFileMemory.cpp',
          'Utility/ROMFileUncompressed.cpp',
          'Utility/Stream.cpp',
          'Utility/StringUtil.cpp',
          'Utility/Synchroniser.cpp',
          'Utility/Timer.cpp',
          'Utility/ZLibWrapper.cpp',
          'ConfigOptions.cpp',
          'System.cpp',

          #FIXME
          'SysW32/DynaRec/x86/AssemblyUtilsX86.cpp',
        ],
        'conditions': [
          ['OS=="win"', {
            'include_dirs': [
              'SysW32/Include',
            ],
            'sources': [
              'SysW32/main.cpp',
              'SysW32/HLEAudio/AudioPluginW32.cpp',
              'SysW32/Debug/DaedalusAssertW32.cpp',
              'SysW32/Debug/DebugConsoleW32.cpp',
              'SysW32/Utility/IOW32.cpp',
              'SysW32/Utility/ThreadW32.cpp',
              'SysW32/Utility/TimingW32.cpp',
            ],
          }],
          ['OS=="mac"', {
            'include_dirs': [
              'SysOSX/Include',
            ],
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/AudioToolbox.framework',
              ],
            },
            'sources': [
              'SysOSX/main.cpp',
              'SysOSX/HLEAudio/AudioPluginOSX.cpp',
              'SysOSX/Debug/DaedalusAssertOSX.cpp',
              'SysOSX/Debug/DebugConsoleOSX.cpp',
              'SysOSX/Debug/WebDebug.cpp',
              'SysOSX/Debug/WebDebugTemplate.cpp',
              'SysOSX/DynaRec/CodeBufferManagerOSX.cpp',
              'SysOSX/HLEGraphics/DisplayListDebugger.cpp',
              'SysOSX/Input/InputManagerOSX.cpp',
              'SysOSX/Utility/IOOSX.cpp',
              'SysOSX/Utility/ThreadOSX.cpp',
              'SysOSX/Utility/TimingOSX.cpp',
            ],
          }],
          ['OS=="linux"', {
            'include_dirs': [
              'SysOSX/Include',
            ],
            'sources': [
              # FIXME - we should move these to a common SysPosix dir...
              'SysOSX/main.cpp',
              'SysOSX/Debug/DaedalusAssertOSX.cpp',
              'SysOSX/Debug/DebugConsoleOSX.cpp',
              'SysOSX/Debug/WebDebug.cpp',
              'SysOSX/Debug/WebDebugTemplate.cpp',
              'SysOSX/DynaRec/CodeBufferManagerOSX.cpp',
              'SysOSX/HLEGraphics/DisplayListDebugger.cpp',
              'SysOSX/Input/InputManagerOSX.cpp',
              'SysOSX/Utility/IOOSX.cpp',
              'SysOSX/Utility/ThreadOSX.cpp',
              'SysOSX/Utility/TimingOSX.cpp',

              'SysLinux/HLEAudio/AudioPluginLinux.cpp',
            ],
          }],
        ],
        'copies': [
          {
            'destination': '<(PRODUCT_DIR)/',
            'files': [
              '../Data/PSP/roms.ini',
            ],
          },
          {
            'destination': '<(PRODUCT_DIR)/',
            'files': [
              'SysOSX/Debug/Web/',
            ],
          },
          {
            'destination': '<(PRODUCT_DIR)/Web/js',
            'files': [
              'SysOSX/Debug/Web/js/dldebugger.js',
            ],
          },
        ],
      },
    ],
  }
