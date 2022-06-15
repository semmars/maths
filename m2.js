'use strict';

var cellArea = (8 / 100000) * (4 / 50000);

//计算的结果

var result = 0;

console.time('Operating time');

// x,y分别代表x,y方向上的第多少份

for (var x = 0; x < 100000; x++) {

    for (var y = 0; y < 50000; y++) {

        //这一份的真实坐标

        var xCoordinate = x / 100000 * 8;

        var yCoordinate = y / 50000 * 4;

        //判断，符合要求则计入面积

        if (xCoordinate <= 4 && yCoordinate / xCoordinate <= 0.5 &&
         Math.sqrt(Math.pow(Math.abs(xCoordinate - 4), 2) + Math.pow(Math.abs(yCoordinate - 4), 2)) >= 4) {

            result += cellArea;
        }
    }
}

//打印结果

console.log('The area under the curve is：' + result);

console.timeEnd('Operating time');