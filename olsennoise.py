#Copyright Tatarize 2014
#MIT License.


def fieldOlsenNoise(x0, y0, x1, y1, iterations):

def singlehash(hash)
    rem = hash & 3;
    h = hash

    switch (rem) {
        case 3:
            hash += h;
            hash ^= hash << 32;
            hash ^= h << 36;
            hash += hash >> 22;
            break;
        case 2:
            hash += h;
            hash ^= hash << 22;
            hash += hash >> 34;
            break;
        case 1:
            hash += h;
            hash ^= hash << 20;
            hash += hash >> 2;
        }
    hash ^= hash << 6;
    hash += hash >> 10;
    hash ^= hash << 8;
    hash += hash >> 34;
    hash ^= hash << 50;
    hash += hash >> 12;
    return hash & 0xFFFF;
    } //provides a hash of a given value.

    hashrandom = function () {
        var hash = singlehash(arguments[0]);
        for (var a = 1; a < arguments.length; a++) {
            hash = singlehash(hash ^ arguments[a]);
        }
        return hash;
    }; //Provides a hashed random value of any number of arguments.
    
    var createArray = function () {
        var arr, len, i;
        if (arguments.length > 0) {
            len = [].slice.call(arguments, 0, 1)[0];
            arr = new Array(len);
            for (i = 0; i < len; i++) {
                arr[i] = createArray.apply(null, [].slice.call(arguments, 1));
            }
        } else {
            return 0;
        }
        return arr;
    }; //creates a zeroed array of given set values.

//OLSEN NOISE
    if (x1 < x0) {
        return null;
    }
    if (y1 < y0) {
        return null;
    }

    var finalwidth = x1 - x0;
    var finalheight = y1 - y0;

    var finalmap = createArray(finalwidth, finalheight);

    if (iterations === 0) {
        var rand;
        for (var j = 0; j < finalwidth; j++) {
            for (var k = 0; k < finalheight; k++) {
                rand = hashrandom(iterations, x0 + j, y0 + k) & (1 << (7 - iterations)); //add noise to map.
                finalmap[j][k] += rand;
            }
        }
        return finalmap;
    }//base case of recurive call is simply random field of 128 and 0.


    var ux0 = Math.floor(x0 / 2) - 1;
    var uy0 = Math.floor(y0 / 2) - 1;
    var ux1 = Math.ceil(x1 / 2) + 1;
    var uy1 = Math.ceil(y1 / 2) + 1;
    //Calculate the size of the image needed to make the size of the image requested.

    var uppermap = fieldOlsenNoise(ux0, uy0, ux1, uy1, iterations - 1);
    //Requests the field of the required size to make the current requested field.
    
    
    var uw = ux1 - ux0;
    var uh = uy1 - uy0;
    //current uppermap width and height.


    var cx0 = ux0 * 2;
    var cy0 = uy0 * 2;
    var cw = uw * 2;
    var ch = uh * 2;
    //scale all the current x,y,w,h to 2x current size for the upsampling.

    var upsampledmap = createArray(cw, ch);
    
    var rand;
    for (var j = 0; j < cw; j++) {
        for (var k = 0; k < ch; k++) {
            rand = (hashrandom(iterations, cx0 + j, cy0 + k) & (1 << (7 - iterations))); //add noise to map.
            upsampledmap[j][k] = uppermap[Math.floor(j / 2)][Math.floor(k / 2)] + rand;
        }
    }//upsampled and random noise addition.

    
        
    var xoff = x0 - cx0;
    var yoff = y0 - cy0;
    //Algorithm must track the position between different requests. x0 is the required value, and cxy is the position of the upper right value in the blurmap.
    
    
    //3x3 box blur will lose two points around edges.
    
    ch-=2;
    for (var j = 0; j < cw; j++) {
        for (var k = 0; k < ch; k++) {
            upsampledmap[j][k] += upsampledmap[j][k+1] + upsampledmap[j][k+2];
        }
    }//blur 1x3
    
    cw-=2;
    for (var k = 0; k < ch; k++) {
        for (var j = 0; j < cw; j++) {
            upsampledmap[j][k] += upsampledmap[j+1][k] + upsampledmap[j+2][k];
        }
    }//blur 1x3

    
    for (var j = 0; j < finalwidth; j++) {
        for (var k = 0; k < finalheight; k++) {
            finalmap[j][k] =  Math.floor(upsampledmap[j + xoff][k + yoff] / 9);
        }
    }//trimmed and positioned.

    return finalmap; //map of correct size is returned.
}