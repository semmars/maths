
var cellArea = (8 / 100000) * (4 / 50000);



//计算的结果

var result = 0;



console.time('Operating time')



// x,y分别代表x,y方向上的第多少份

for (let x = 0; x < 100000; x++) {

    for (let y = 0; y < 50000; y++) {



        //这一份的真实坐标

        let xCoordinate = (x / 100000) * 8;

        let yCoordinate = (y / 50000) * 4;



        //判断，符合要求则计入面积

        if (

            xCoordinate <= 4 &&

            (yCoordinate / xCoordinate) <= 0.5 &&

            Math.sqrt((Math.abs(xCoordinate - 4) ** 2) + (Math.abs(yCoordinate - 4) ** 2)) >= 4

        ) {

            result += cellArea;

        }

    }

}



//打印结果

console.log('The area under the curve is：' + result)

console.timeEnd('Operating time')

