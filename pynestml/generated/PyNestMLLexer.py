# Generated from PyNestMLLexer.g4 by ANTLR 4.10
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if __name__ is not None and "." in __name__:
    from .PyNestMLLexerBase import PyNestMLLexerBase
else:
    from PyNestMLLexerBase import PyNestMLLexerBase

def serializedATN():
    return [
        4,0,90,699,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,1,0,1,0,1,0,1,0,1,1,3,1,191,8,1,1,1,1,1,1,2,1,2,1,2,3,2,
        198,8,2,1,3,4,3,201,8,3,11,3,12,3,202,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,5,5,214,8,5,10,5,12,5,217,9,5,1,5,1,5,4,5,221,8,5,11,5,
        12,5,222,1,5,1,5,1,6,1,6,5,6,229,8,6,10,6,12,6,232,9,6,1,6,1,6,1,
        7,1,7,1,7,3,7,239,8,7,1,7,1,7,1,7,3,7,244,8,7,3,7,246,8,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,
        1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,
        1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,46,1,46,1,46,1,46,
        1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,
        1,53,1,54,1,54,1,55,1,55,1,55,1,56,1,56,1,57,1,57,1,57,1,58,1,58,
        1,58,1,59,1,59,1,59,1,60,1,60,1,60,1,61,1,61,1,62,1,62,1,63,1,63,
        1,63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,1,67,
        1,68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,71,1,72,
        1,72,1,73,1,73,1,74,1,74,1,75,1,75,1,76,1,76,1,76,1,77,1,77,1,78,
        1,78,1,79,1,79,1,80,1,80,1,81,1,81,1,81,1,82,1,82,1,83,1,83,1,84,
        1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,84,
        1,84,1,84,1,84,1,84,3,84,633,8,84,1,85,1,85,1,85,4,85,638,8,85,11,
        85,12,85,639,1,85,3,85,643,8,85,1,85,3,85,646,8,85,1,85,3,85,649,
        8,85,1,85,5,85,652,8,85,10,85,12,85,655,9,85,1,85,1,85,1,86,3,86,
        660,8,86,1,86,5,86,663,8,86,10,86,12,86,666,9,86,1,87,4,87,669,8,
        87,11,87,12,87,670,1,88,1,88,3,88,675,8,88,1,89,3,89,678,8,89,1,
        89,1,89,1,89,1,89,1,89,3,89,685,8,89,1,90,1,90,3,90,689,8,90,1,90,
        1,90,1,90,1,91,1,91,3,91,696,8,91,1,91,1,91,2,215,222,0,92,1,3,3,
        0,5,4,7,5,9,6,11,7,13,8,15,9,17,10,19,11,21,12,23,13,25,14,27,15,
        29,16,31,17,33,18,35,19,37,20,39,21,41,22,43,23,45,24,47,25,49,26,
        51,27,53,28,55,29,57,30,59,31,61,32,63,33,65,34,67,35,69,36,71,37,
        73,38,75,39,77,40,79,41,81,42,83,43,85,44,87,45,89,46,91,47,93,48,
        95,49,97,50,99,51,101,52,103,53,105,54,107,55,109,56,111,57,113,
        58,115,59,117,60,119,61,121,62,123,63,125,64,127,65,129,66,131,67,
        133,68,135,69,137,70,139,71,141,72,143,73,145,74,147,75,149,76,151,
        77,153,78,155,79,157,80,159,81,161,82,163,83,165,84,167,85,169,86,
        171,87,173,88,175,89,177,90,179,0,181,0,183,0,1,0,7,2,0,9,9,32,32,
        2,0,10,10,13,13,4,0,10,10,13,13,34,34,92,92,4,0,36,36,65,90,95,95,
        97,122,5,0,36,36,48,57,65,90,95,95,97,122,1,0,48,57,2,0,69,69,101,
        101,720,0,1,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,
        0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,
        0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,
        0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,
        0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,
        0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,
        0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,
        111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,
        0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,
        1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,
        0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,
        0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,
        157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,
        0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,175,
        1,0,0,0,0,177,1,0,0,0,1,185,1,0,0,0,3,190,1,0,0,0,5,194,1,0,0,0,
        7,200,1,0,0,0,9,206,1,0,0,0,11,211,1,0,0,0,13,226,1,0,0,0,15,245,
        1,0,0,0,17,249,1,0,0,0,19,257,1,0,0,0,21,262,1,0,0,0,23,269,1,0,
        0,0,25,277,1,0,0,0,27,282,1,0,0,0,29,291,1,0,0,0,31,298,1,0,0,0,
        33,305,1,0,0,0,35,308,1,0,0,0,37,313,1,0,0,0,39,318,1,0,0,0,41,322,
        1,0,0,0,43,328,1,0,0,0,45,331,1,0,0,0,47,336,1,0,0,0,49,340,1,0,
        0,0,51,344,1,0,0,0,53,347,1,0,0,0,55,351,1,0,0,0,57,362,1,0,0,0,
        59,369,1,0,0,0,61,376,1,0,0,0,63,384,1,0,0,0,65,390,1,0,0,0,67,401,
        1,0,0,0,69,411,1,0,0,0,71,418,1,0,0,0,73,428,1,0,0,0,75,434,1,0,
        0,0,77,441,1,0,0,0,79,452,1,0,0,0,81,462,1,0,0,0,83,468,1,0,0,0,
        85,479,1,0,0,0,87,490,1,0,0,0,89,503,1,0,0,0,91,518,1,0,0,0,93,520,
        1,0,0,0,95,524,1,0,0,0,97,526,1,0,0,0,99,528,1,0,0,0,101,530,1,0,
        0,0,103,532,1,0,0,0,105,534,1,0,0,0,107,536,1,0,0,0,109,538,1,0,
        0,0,111,540,1,0,0,0,113,543,1,0,0,0,115,545,1,0,0,0,117,548,1,0,
        0,0,119,551,1,0,0,0,121,554,1,0,0,0,123,557,1,0,0,0,125,559,1,0,
        0,0,127,561,1,0,0,0,129,564,1,0,0,0,131,567,1,0,0,0,133,570,1,0,
        0,0,135,573,1,0,0,0,137,576,1,0,0,0,139,579,1,0,0,0,141,582,1,0,
        0,0,143,585,1,0,0,0,145,588,1,0,0,0,147,590,1,0,0,0,149,592,1,0,
        0,0,151,594,1,0,0,0,153,596,1,0,0,0,155,599,1,0,0,0,157,601,1,0,
        0,0,159,603,1,0,0,0,161,605,1,0,0,0,163,607,1,0,0,0,165,610,1,0,
        0,0,167,612,1,0,0,0,169,632,1,0,0,0,171,634,1,0,0,0,173,659,1,0,
        0,0,175,668,1,0,0,0,177,674,1,0,0,0,179,684,1,0,0,0,181,688,1,0,
        0,0,183,695,1,0,0,0,185,186,5,34,0,0,186,187,5,34,0,0,187,188,5,
        34,0,0,188,2,1,0,0,0,189,191,5,13,0,0,190,189,1,0,0,0,190,191,1,
        0,0,0,191,192,1,0,0,0,192,193,5,10,0,0,193,4,1,0,0,0,194,195,3,145,
        72,0,195,197,3,3,1,0,196,198,3,7,3,0,197,196,1,0,0,0,197,198,1,0,
        0,0,198,6,1,0,0,0,199,201,7,0,0,0,200,199,1,0,0,0,201,202,1,0,0,
        0,202,200,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,6,3,0,
        0,205,8,1,0,0,0,206,207,5,92,0,0,207,208,3,3,1,0,208,209,1,0,0,0,
        209,210,6,4,0,0,210,10,1,0,0,0,211,215,3,1,0,0,212,214,9,0,0,0,213,
        212,1,0,0,0,214,217,1,0,0,0,215,216,1,0,0,0,215,213,1,0,0,0,216,
        218,1,0,0,0,217,215,1,0,0,0,218,220,3,1,0,0,219,221,3,3,1,0,220,
        219,1,0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,222,220,1,0,0,0,223,
        224,1,0,0,0,224,225,6,5,1,0,225,12,1,0,0,0,226,230,5,35,0,0,227,
        229,8,1,0,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,
        231,1,0,0,0,231,233,1,0,0,0,232,230,1,0,0,0,233,234,6,6,1,0,234,
        14,1,0,0,0,235,236,4,7,0,0,236,246,3,7,3,0,237,239,5,13,0,0,238,
        237,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,10,0,0,241,
        243,1,0,0,0,242,244,3,7,3,0,243,242,1,0,0,0,243,244,1,0,0,0,244,
        246,1,0,0,0,245,235,1,0,0,0,245,238,1,0,0,0,246,247,1,0,0,0,247,
        248,6,7,2,0,248,16,1,0,0,0,249,250,5,105,0,0,250,251,5,110,0,0,251,
        252,5,116,0,0,252,253,5,101,0,0,253,254,5,103,0,0,254,255,5,101,
        0,0,255,256,5,114,0,0,256,18,1,0,0,0,257,258,5,114,0,0,258,259,5,
        101,0,0,259,260,5,97,0,0,260,261,5,108,0,0,261,20,1,0,0,0,262,263,
        5,115,0,0,263,264,5,116,0,0,264,265,5,114,0,0,265,266,5,105,0,0,
        266,267,5,110,0,0,267,268,5,103,0,0,268,22,1,0,0,0,269,270,5,98,
        0,0,270,271,5,111,0,0,271,272,5,111,0,0,272,273,5,108,0,0,273,274,
        5,101,0,0,274,275,5,97,0,0,275,276,5,110,0,0,276,24,1,0,0,0,277,
        278,5,118,0,0,278,279,5,111,0,0,279,280,5,105,0,0,280,281,5,100,
        0,0,281,26,1,0,0,0,282,283,5,102,0,0,283,284,5,117,0,0,284,285,5,
        110,0,0,285,286,5,99,0,0,286,287,5,116,0,0,287,288,5,105,0,0,288,
        289,5,111,0,0,289,290,5,110,0,0,290,28,1,0,0,0,291,292,5,105,0,0,
        292,293,5,110,0,0,293,294,5,108,0,0,294,295,5,105,0,0,295,296,5,
        110,0,0,296,297,5,101,0,0,297,30,1,0,0,0,298,299,5,114,0,0,299,300,
        5,101,0,0,300,301,5,116,0,0,301,302,5,117,0,0,302,303,5,114,0,0,
        303,304,5,110,0,0,304,32,1,0,0,0,305,306,5,105,0,0,306,307,5,102,
        0,0,307,34,1,0,0,0,308,309,5,101,0,0,309,310,5,108,0,0,310,311,5,
        105,0,0,311,312,5,102,0,0,312,36,1,0,0,0,313,314,5,101,0,0,314,315,
        5,108,0,0,315,316,5,115,0,0,316,317,5,101,0,0,317,38,1,0,0,0,318,
        319,5,102,0,0,319,320,5,111,0,0,320,321,5,114,0,0,321,40,1,0,0,0,
        322,323,5,119,0,0,323,324,5,104,0,0,324,325,5,105,0,0,325,326,5,
        108,0,0,326,327,5,101,0,0,327,42,1,0,0,0,328,329,5,105,0,0,329,330,
        5,110,0,0,330,44,1,0,0,0,331,332,5,115,0,0,332,333,5,116,0,0,333,
        334,5,101,0,0,334,335,5,112,0,0,335,46,1,0,0,0,336,337,5,105,0,0,
        337,338,5,110,0,0,338,339,5,102,0,0,339,48,1,0,0,0,340,341,5,97,
        0,0,341,342,5,110,0,0,342,343,5,100,0,0,343,50,1,0,0,0,344,345,5,
        111,0,0,345,346,5,114,0,0,346,52,1,0,0,0,347,348,5,110,0,0,348,349,
        5,111,0,0,349,350,5,116,0,0,350,54,1,0,0,0,351,352,5,114,0,0,352,
        353,5,101,0,0,353,354,5,99,0,0,354,355,5,111,0,0,355,356,5,114,0,
        0,356,357,5,100,0,0,357,358,5,97,0,0,358,359,5,98,0,0,359,360,5,
        108,0,0,360,361,5,101,0,0,361,56,1,0,0,0,362,363,5,107,0,0,363,364,
        5,101,0,0,364,365,5,114,0,0,365,366,5,110,0,0,366,367,5,101,0,0,
        367,368,5,108,0,0,368,58,1,0,0,0,369,370,5,110,0,0,370,371,5,101,
        0,0,371,372,5,117,0,0,372,373,5,114,0,0,373,374,5,111,0,0,374,375,
        5,110,0,0,375,60,1,0,0,0,376,377,5,115,0,0,377,378,5,121,0,0,378,
        379,5,110,0,0,379,380,5,97,0,0,380,381,5,112,0,0,381,382,5,115,0,
        0,382,383,5,101,0,0,383,62,1,0,0,0,384,385,5,115,0,0,385,386,5,116,
        0,0,386,387,5,97,0,0,387,388,5,116,0,0,388,389,5,101,0,0,389,64,
        1,0,0,0,390,391,5,112,0,0,391,392,5,97,0,0,392,393,5,114,0,0,393,
        394,5,97,0,0,394,395,5,109,0,0,395,396,5,101,0,0,396,397,5,116,0,
        0,397,398,5,101,0,0,398,399,5,114,0,0,399,400,5,115,0,0,400,66,1,
        0,0,0,401,402,5,105,0,0,402,403,5,110,0,0,403,404,5,116,0,0,404,
        405,5,101,0,0,405,406,5,114,0,0,406,407,5,110,0,0,407,408,5,97,0,
        0,408,409,5,108,0,0,409,410,5,115,0,0,410,68,1,0,0,0,411,412,5,117,
        0,0,412,413,5,112,0,0,413,414,5,100,0,0,414,415,5,97,0,0,415,416,
        5,116,0,0,416,417,5,101,0,0,417,70,1,0,0,0,418,419,5,101,0,0,419,
        420,5,113,0,0,420,421,5,117,0,0,421,422,5,97,0,0,422,423,5,116,0,
        0,423,424,5,105,0,0,424,425,5,111,0,0,425,426,5,110,0,0,426,427,
        5,115,0,0,427,72,1,0,0,0,428,429,5,105,0,0,429,430,5,110,0,0,430,
        431,5,112,0,0,431,432,5,117,0,0,432,433,5,116,0,0,433,74,1,0,0,0,
        434,435,5,111,0,0,435,436,5,117,0,0,436,437,5,116,0,0,437,438,5,
        112,0,0,438,439,5,117,0,0,439,440,5,116,0,0,440,76,1,0,0,0,441,442,
        5,99,0,0,442,443,5,111,0,0,443,444,5,110,0,0,444,445,5,116,0,0,445,
        446,5,105,0,0,446,447,5,110,0,0,447,448,5,117,0,0,448,449,5,111,
        0,0,449,450,5,117,0,0,450,451,5,115,0,0,451,78,1,0,0,0,452,453,5,
        111,0,0,453,454,5,110,0,0,454,455,5,82,0,0,455,456,5,101,0,0,456,
        457,5,99,0,0,457,458,5,101,0,0,458,459,5,105,0,0,459,460,5,118,0,
        0,460,461,5,101,0,0,461,80,1,0,0,0,462,463,5,115,0,0,463,464,5,112,
        0,0,464,465,5,105,0,0,465,466,5,107,0,0,466,467,5,101,0,0,467,82,
        1,0,0,0,468,469,5,105,0,0,469,470,5,110,0,0,470,471,5,104,0,0,471,
        472,5,105,0,0,472,473,5,98,0,0,473,474,5,105,0,0,474,475,5,116,0,
        0,475,476,5,111,0,0,476,477,5,114,0,0,477,478,5,121,0,0,478,84,1,
        0,0,0,479,480,5,101,0,0,480,481,5,120,0,0,481,482,5,99,0,0,482,483,
        5,105,0,0,483,484,5,116,0,0,484,485,5,97,0,0,485,486,5,116,0,0,486,
        487,5,111,0,0,487,488,5,114,0,0,488,489,5,121,0,0,489,86,1,0,0,0,
        490,491,5,64,0,0,491,492,5,104,0,0,492,493,5,111,0,0,493,494,5,109,
        0,0,494,495,5,111,0,0,495,496,5,103,0,0,496,497,5,101,0,0,497,498,
        5,110,0,0,498,499,5,101,0,0,499,500,5,111,0,0,500,501,5,117,0,0,
        501,502,5,115,0,0,502,88,1,0,0,0,503,504,5,64,0,0,504,505,5,104,
        0,0,505,506,5,101,0,0,506,507,5,116,0,0,507,508,5,101,0,0,508,509,
        5,114,0,0,509,510,5,111,0,0,510,511,5,103,0,0,511,512,5,101,0,0,
        512,513,5,110,0,0,513,514,5,101,0,0,514,515,5,111,0,0,515,516,5,
        117,0,0,516,517,5,115,0,0,517,90,1,0,0,0,518,519,5,64,0,0,519,92,
        1,0,0,0,520,521,5,46,0,0,521,522,5,46,0,0,522,523,5,46,0,0,523,94,
        1,0,0,0,524,525,5,40,0,0,525,96,1,0,0,0,526,527,5,41,0,0,527,98,
        1,0,0,0,528,529,5,43,0,0,529,100,1,0,0,0,530,531,5,126,0,0,531,102,
        1,0,0,0,532,533,5,124,0,0,533,104,1,0,0,0,534,535,5,94,0,0,535,106,
        1,0,0,0,536,537,5,38,0,0,537,108,1,0,0,0,538,539,5,91,0,0,539,110,
        1,0,0,0,540,541,5,60,0,0,541,542,5,45,0,0,542,112,1,0,0,0,543,544,
        5,93,0,0,544,114,1,0,0,0,545,546,5,91,0,0,546,547,5,91,0,0,547,116,
        1,0,0,0,548,549,5,93,0,0,549,550,5,93,0,0,550,118,1,0,0,0,551,552,
        5,60,0,0,552,553,5,60,0,0,553,120,1,0,0,0,554,555,5,62,0,0,555,556,
        5,62,0,0,556,122,1,0,0,0,557,558,5,60,0,0,558,124,1,0,0,0,559,560,
        5,62,0,0,560,126,1,0,0,0,561,562,5,60,0,0,562,563,5,61,0,0,563,128,
        1,0,0,0,564,565,5,43,0,0,565,566,5,61,0,0,566,130,1,0,0,0,567,568,
        5,45,0,0,568,569,5,61,0,0,569,132,1,0,0,0,570,571,5,42,0,0,571,572,
        5,61,0,0,572,134,1,0,0,0,573,574,5,47,0,0,574,575,5,61,0,0,575,136,
        1,0,0,0,576,577,5,61,0,0,577,578,5,61,0,0,578,138,1,0,0,0,579,580,
        5,33,0,0,580,581,5,61,0,0,581,140,1,0,0,0,582,583,5,60,0,0,583,584,
        5,62,0,0,584,142,1,0,0,0,585,586,5,62,0,0,586,587,5,61,0,0,587,144,
        1,0,0,0,588,589,5,44,0,0,589,146,1,0,0,0,590,591,5,45,0,0,591,148,
        1,0,0,0,592,593,5,61,0,0,593,150,1,0,0,0,594,595,5,42,0,0,595,152,
        1,0,0,0,596,597,5,42,0,0,597,598,5,42,0,0,598,154,1,0,0,0,599,600,
        5,47,0,0,600,156,1,0,0,0,601,602,5,37,0,0,602,158,1,0,0,0,603,604,
        5,63,0,0,604,160,1,0,0,0,605,606,5,58,0,0,606,162,1,0,0,0,607,608,
        5,58,0,0,608,609,5,58,0,0,609,164,1,0,0,0,610,611,5,59,0,0,611,166,
        1,0,0,0,612,613,5,39,0,0,613,168,1,0,0,0,614,615,5,116,0,0,615,616,
        5,114,0,0,616,617,5,117,0,0,617,633,5,101,0,0,618,619,5,84,0,0,619,
        620,5,114,0,0,620,621,5,117,0,0,621,633,5,101,0,0,622,623,5,102,
        0,0,623,624,5,97,0,0,624,625,5,108,0,0,625,626,5,115,0,0,626,633,
        5,101,0,0,627,628,5,70,0,0,628,629,5,97,0,0,629,630,5,108,0,0,630,
        631,5,115,0,0,631,633,5,101,0,0,632,614,1,0,0,0,632,618,1,0,0,0,
        632,622,1,0,0,0,632,627,1,0,0,0,633,170,1,0,0,0,634,653,5,34,0,0,
        635,648,5,92,0,0,636,638,7,0,0,0,637,636,1,0,0,0,638,639,1,0,0,0,
        639,637,1,0,0,0,639,640,1,0,0,0,640,645,1,0,0,0,641,643,5,13,0,0,
        642,641,1,0,0,0,642,643,1,0,0,0,643,644,1,0,0,0,644,646,5,10,0,0,
        645,642,1,0,0,0,645,646,1,0,0,0,646,649,1,0,0,0,647,649,9,0,0,0,
        648,637,1,0,0,0,648,647,1,0,0,0,649,652,1,0,0,0,650,652,8,2,0,0,
        651,635,1,0,0,0,651,650,1,0,0,0,652,655,1,0,0,0,653,651,1,0,0,0,
        653,654,1,0,0,0,654,656,1,0,0,0,655,653,1,0,0,0,656,657,5,34,0,0,
        657,172,1,0,0,0,658,660,7,3,0,0,659,658,1,0,0,0,660,664,1,0,0,0,
        661,663,7,4,0,0,662,661,1,0,0,0,663,666,1,0,0,0,664,662,1,0,0,0,
        664,665,1,0,0,0,665,174,1,0,0,0,666,664,1,0,0,0,667,669,7,5,0,0,
        668,667,1,0,0,0,669,670,1,0,0,0,670,668,1,0,0,0,670,671,1,0,0,0,
        671,176,1,0,0,0,672,675,3,179,89,0,673,675,3,181,90,0,674,672,1,
        0,0,0,674,673,1,0,0,0,675,178,1,0,0,0,676,678,3,175,87,0,677,676,
        1,0,0,0,677,678,1,0,0,0,678,679,1,0,0,0,679,680,5,46,0,0,680,685,
        3,175,87,0,681,682,3,175,87,0,682,683,5,46,0,0,683,685,1,0,0,0,684,
        677,1,0,0,0,684,681,1,0,0,0,685,180,1,0,0,0,686,689,3,175,87,0,687,
        689,3,179,89,0,688,686,1,0,0,0,688,687,1,0,0,0,689,690,1,0,0,0,690,
        691,7,6,0,0,691,692,3,183,91,0,692,182,1,0,0,0,693,696,3,99,49,0,
        694,696,3,147,73,0,695,693,1,0,0,0,695,694,1,0,0,0,695,696,1,0,0,
        0,696,697,1,0,0,0,697,698,3,175,87,0,698,184,1,0,0,0,26,0,190,197,
        202,215,222,230,238,243,245,632,639,642,645,648,651,653,659,662,
        664,670,674,677,684,688,695,3,0,1,0,0,2,0,1,7,0
    ]

class PyNestMLLexer(PyNestMLLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 2

    INDENT = 1
    DEDENT = 2
    DOCSTRING_TRIPLEQUOTE = 3
    KERNEL_JOINING = 4
    WS = 5
    LINE_ESCAPE = 6
    DOCSTRING = 7
    SL_COMMENT = 8
    NEWLINE = 9
    INTEGER_KEYWORD = 10
    REAL_KEYWORD = 11
    STRING_KEYWORD = 12
    BOOLEAN_KEYWORD = 13
    VOID_KEYWORD = 14
    FUNCTION_KEYWORD = 15
    INLINE_KEYWORD = 16
    RETURN_KEYWORD = 17
    IF_KEYWORD = 18
    ELIF_KEYWORD = 19
    ELSE_KEYWORD = 20
    FOR_KEYWORD = 21
    WHILE_KEYWORD = 22
    IN_KEYWORD = 23
    STEP_KEYWORD = 24
    INF_KEYWORD = 25
    AND_KEYWORD = 26
    OR_KEYWORD = 27
    NOT_KEYWORD = 28
    RECORDABLE_KEYWORD = 29
    KERNEL_KEYWORD = 30
    NEURON_KEYWORD = 31
    SYNAPSE_KEYWORD = 32
    STATE_KEYWORD = 33
    PARAMETERS_KEYWORD = 34
    INTERNALS_KEYWORD = 35
    UPDATE_KEYWORD = 36
    EQUATIONS_KEYWORD = 37
    INPUT_KEYWORD = 38
    OUTPUT_KEYWORD = 39
    CONTINUOUS_KEYWORD = 40
    ON_RECEIVE_KEYWORD = 41
    SPIKE_KEYWORD = 42
    INHIBITORY_KEYWORD = 43
    EXCITATORY_KEYWORD = 44
    DECORATOR_HOMOGENEOUS = 45
    DECORATOR_HETEROGENEOUS = 46
    AT = 47
    ELLIPSIS = 48
    LEFT_PAREN = 49
    RIGHT_PAREN = 50
    PLUS = 51
    TILDE = 52
    PIPE = 53
    CARET = 54
    AMPERSAND = 55
    LEFT_SQUARE_BRACKET = 56
    LEFT_ANGLE_MINUS = 57
    RIGHT_SQUARE_BRACKET = 58
    LEFT_LEFT_SQUARE = 59
    RIGHT_RIGHT_SQUARE = 60
    LEFT_LEFT_ANGLE = 61
    RIGHT_RIGHT_ANGLE = 62
    LEFT_ANGLE = 63
    RIGHT_ANGLE = 64
    LEFT_ANGLE_EQUALS = 65
    PLUS_EQUALS = 66
    MINUS_EQUALS = 67
    STAR_EQUALS = 68
    FORWARD_SLASH_EQUALS = 69
    EQUALS_EQUALS = 70
    EXCLAMATION_EQUALS = 71
    LEFT_ANGLE_RIGHT_ANGLE = 72
    RIGHT_ANGLE_EQUALS = 73
    COMMA = 74
    MINUS = 75
    EQUALS = 76
    STAR = 77
    STAR_STAR = 78
    FORWARD_SLASH = 79
    PERCENT = 80
    QUESTION = 81
    COLON = 82
    DOUBLE_COLON = 83
    SEMICOLON = 84
    DIFFERENTIAL_ORDER = 85
    BOOLEAN_LITERAL = 86
    STRING_LITERAL = 87
    NAME = 88
    UNSIGNED_INTEGER = 89
    FLOAT = 90

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"COMMENT" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"\"\"'", "'integer'", "'real'", "'string'", "'boolean'", 
            "'void'", "'function'", "'inline'", "'return'", "'if'", "'elif'", 
            "'else'", "'for'", "'while'", "'in'", "'step'", "'inf'", "'and'", 
            "'or'", "'not'", "'recordable'", "'kernel'", "'neuron'", "'synapse'", 
            "'state'", "'parameters'", "'internals'", "'update'", "'equations'", 
            "'input'", "'output'", "'continuous'", "'onReceive'", "'spike'", 
            "'inhibitory'", "'excitatory'", "'@homogeneous'", "'@heterogeneous'", 
            "'@'", "'...'", "'('", "')'", "'+'", "'~'", "'|'", "'^'", "'&'", 
            "'['", "'<-'", "']'", "'[['", "']]'", "'<<'", "'>>'", "'<'", 
            "'>'", "'<='", "'+='", "'-='", "'*='", "'/='", "'=='", "'!='", 
            "'<>'", "'>='", "','", "'-'", "'='", "'*'", "'**'", "'/'", "'%'", 
            "'?'", "':'", "'::'", "';'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "DOCSTRING_TRIPLEQUOTE", "KERNEL_JOINING", 
            "WS", "LINE_ESCAPE", "DOCSTRING", "SL_COMMENT", "NEWLINE", "INTEGER_KEYWORD", 
            "REAL_KEYWORD", "STRING_KEYWORD", "BOOLEAN_KEYWORD", "VOID_KEYWORD", 
            "FUNCTION_KEYWORD", "INLINE_KEYWORD", "RETURN_KEYWORD", "IF_KEYWORD", 
            "ELIF_KEYWORD", "ELSE_KEYWORD", "FOR_KEYWORD", "WHILE_KEYWORD", 
            "IN_KEYWORD", "STEP_KEYWORD", "INF_KEYWORD", "AND_KEYWORD", 
            "OR_KEYWORD", "NOT_KEYWORD", "RECORDABLE_KEYWORD", "KERNEL_KEYWORD", 
            "NEURON_KEYWORD", "SYNAPSE_KEYWORD", "STATE_KEYWORD", "PARAMETERS_KEYWORD", 
            "INTERNALS_KEYWORD", "UPDATE_KEYWORD", "EQUATIONS_KEYWORD", 
            "INPUT_KEYWORD", "OUTPUT_KEYWORD", "CONTINUOUS_KEYWORD", "ON_RECEIVE_KEYWORD", 
            "SPIKE_KEYWORD", "INHIBITORY_KEYWORD", "EXCITATORY_KEYWORD", 
            "DECORATOR_HOMOGENEOUS", "DECORATOR_HETEROGENEOUS", "AT", "ELLIPSIS", 
            "LEFT_PAREN", "RIGHT_PAREN", "PLUS", "TILDE", "PIPE", "CARET", 
            "AMPERSAND", "LEFT_SQUARE_BRACKET", "LEFT_ANGLE_MINUS", "RIGHT_SQUARE_BRACKET", 
            "LEFT_LEFT_SQUARE", "RIGHT_RIGHT_SQUARE", "LEFT_LEFT_ANGLE", 
            "RIGHT_RIGHT_ANGLE", "LEFT_ANGLE", "RIGHT_ANGLE", "LEFT_ANGLE_EQUALS", 
            "PLUS_EQUALS", "MINUS_EQUALS", "STAR_EQUALS", "FORWARD_SLASH_EQUALS", 
            "EQUALS_EQUALS", "EXCLAMATION_EQUALS", "LEFT_ANGLE_RIGHT_ANGLE", 
            "RIGHT_ANGLE_EQUALS", "COMMA", "MINUS", "EQUALS", "STAR", "STAR_STAR", 
            "FORWARD_SLASH", "PERCENT", "QUESTION", "COLON", "DOUBLE_COLON", 
            "SEMICOLON", "DIFFERENTIAL_ORDER", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "NAME", "UNSIGNED_INTEGER", "FLOAT" ]

    ruleNames = [ "DOCSTRING_TRIPLEQUOTE", "NEWLINE_FRAG", "KERNEL_JOINING", 
                  "WS", "LINE_ESCAPE", "DOCSTRING", "SL_COMMENT", "NEWLINE", 
                  "INTEGER_KEYWORD", "REAL_KEYWORD", "STRING_KEYWORD", "BOOLEAN_KEYWORD", 
                  "VOID_KEYWORD", "FUNCTION_KEYWORD", "INLINE_KEYWORD", 
                  "RETURN_KEYWORD", "IF_KEYWORD", "ELIF_KEYWORD", "ELSE_KEYWORD", 
                  "FOR_KEYWORD", "WHILE_KEYWORD", "IN_KEYWORD", "STEP_KEYWORD", 
                  "INF_KEYWORD", "AND_KEYWORD", "OR_KEYWORD", "NOT_KEYWORD", 
                  "RECORDABLE_KEYWORD", "KERNEL_KEYWORD", "NEURON_KEYWORD", 
                  "SYNAPSE_KEYWORD", "STATE_KEYWORD", "PARAMETERS_KEYWORD", 
                  "INTERNALS_KEYWORD", "UPDATE_KEYWORD", "EQUATIONS_KEYWORD", 
                  "INPUT_KEYWORD", "OUTPUT_KEYWORD", "CONTINUOUS_KEYWORD", 
                  "ON_RECEIVE_KEYWORD", "SPIKE_KEYWORD", "INHIBITORY_KEYWORD", 
                  "EXCITATORY_KEYWORD", "DECORATOR_HOMOGENEOUS", "DECORATOR_HETEROGENEOUS", 
                  "AT", "ELLIPSIS", "LEFT_PAREN", "RIGHT_PAREN", "PLUS", 
                  "TILDE", "PIPE", "CARET", "AMPERSAND", "LEFT_SQUARE_BRACKET", 
                  "LEFT_ANGLE_MINUS", "RIGHT_SQUARE_BRACKET", "LEFT_LEFT_SQUARE", 
                  "RIGHT_RIGHT_SQUARE", "LEFT_LEFT_ANGLE", "RIGHT_RIGHT_ANGLE", 
                  "LEFT_ANGLE", "RIGHT_ANGLE", "LEFT_ANGLE_EQUALS", "PLUS_EQUALS", 
                  "MINUS_EQUALS", "STAR_EQUALS", "FORWARD_SLASH_EQUALS", 
                  "EQUALS_EQUALS", "EXCLAMATION_EQUALS", "LEFT_ANGLE_RIGHT_ANGLE", 
                  "RIGHT_ANGLE_EQUALS", "COMMA", "MINUS", "EQUALS", "STAR", 
                  "STAR_STAR", "FORWARD_SLASH", "PERCENT", "QUESTION", "COLON", 
                  "DOUBLE_COLON", "SEMICOLON", "DIFFERENTIAL_ORDER", "BOOLEAN_LITERAL", 
                  "STRING_LITERAL", "NAME", "UNSIGNED_INTEGER", "FLOAT", 
                  "POINT_FLOAT", "EXPONENT_FLOAT", "EXPONENT" ]

    grammarFileName = "PyNestMLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.onNewLine()
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[7] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


