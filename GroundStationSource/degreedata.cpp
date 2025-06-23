#include "degreedata.h"

#include <stdlib.h>

#include "raylib.h"

int degreenum() {
    _sleep(1000);
    return GetRandomValue(1, 100); // 1 ile 100 arasında rastgele derece
}
