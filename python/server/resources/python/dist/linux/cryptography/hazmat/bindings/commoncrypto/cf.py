# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <CoreFoundation/CoreFoundation.h>
"""

TYPES = """
typedef bool Boolean;
typedef signed long OSStatus;
typedef unsigned char UInt8;
typedef uint32_t UInt32;

typedef const void * CFAllocatorRef;
const CFAllocatorRef kCFAllocatorDefault;
typedef const void * CFDataRef;
typedef signed long long CFIndex;
typedef ... *CFStringRef;
typedef ... *CFArrayRef;
typedef ... *CFBooleanRef;
typedef ... *CFErrorRef;
typedef ... *CFNumberRef;
typedef ... *CFTypeRef;
typedef ... *CFDictionaryRef;
typedef ... *CFMutableDictionaryRef;
typedef struct {
    ...;
} CFDictionaryKeyCallBacks;
typedef struct {
    ...;
} CFDictionaryValueCallBacks;
typedef struct {
    ...;
} CFRange;

typedef UInt32 CFStringEncoding;
enum {
    kCFStringEncodingASCII = 0x0600
};

enum {
   kCFNumberSInt8Type = 1,
   kCFNumberSInt16Type = 2,
   kCFNumberSInt32Type = 3,
   kCFNumberSInt64Type = 4,
   kCFNumberFloat32Type = 5,
   kCFNumberFloat64Type = 6,
   kCFNumberCharType = 7,
   kCFNumberShortType = 8,
   kCFNumberIntType = 9,
   kCFNumberLongType = 10,
   kCFNumberLongLongType = 11,
   kCFNumberFloatType = 12,
   kCFNumberDoubleType = 13,
   kCFNumberCFIndexType = 14,
   kCFNumberNSIntegerType = 15,
   kCFNumberCGFloatType = 16,
   kCFNumberMaxType = 16
};
typedef int CFNumberType;

const CFDictionaryKeyCallBacks kCFTypeDictionaryKeyCallBacks;
const CFDictionaryValueCallBacks kCFTypeDictionaryValueCallBacks;

const CFBooleanRef kCFBooleanTrue;
const CFBooleanRef kCFBooleanFalse;
"""

FUNCTIONS = """
CFDataRef CFDataCreate(CFAllocatorRef, const UInt8 *, CFIndex);
CFStringRef CFStringCreateWithCString(CFAllocatorRef, const char *,
                                      CFStringEncoding);
CFDictionaryRef CFDictionaryCreate(CFAllocatorRef, const void **,
                                   const void **, CFIndex,
                                   const CFDictionaryKeyCallBacks *,
                                   const CFDictionaryValueCallBacks *);
CFMutableDictionaryRef CFDictionaryCreateMutable(
    CFAllocatorRef,
    CFIndex,
    const CFDictionaryKeyCallBacks *,
    const CFDictionaryValueCallBacks *
);
void CFDictionarySetValue(CFMutableDictionaryRef, const void *, const void *);
CFIndex CFArrayGetCount(CFArrayRef);
const void *CFArrayGetValueAtIndex(CFArrayRef, CFIndex);
CFIndex CFDataGetLength(CFDataRef);
void CFDataGetBytes(CFDataRef, CFRange, UInt8 *);
CFRange CFRangeMake(CFIndex, CFIndex);
void CFShow(CFTypeRef);
Boolean CFBooleanGetValue(CFBooleanRef);
CFNumberRef CFNumberCreate(CFAllocatorRef, CFNumberType, const void *);
void CFRelease(CFTypeRef);
CFTypeRef CFRetain(CFTypeRef);
"""

MACROS = """
"""

CUSTOMIZATIONS = """
"""

CONDITIONAL_NAMES = {}
