let canvas = document.getElementById("imageCanvas");
let canvasContext = canvas.getContext("2d");
let canvasShadow = canvas.cloneNode();
let canvasContextShadow = canvasShadow.getContext("2d");

function SaveCanvas() {
  canvasContextShadow.clearRect(0, 0, canvasShadow.width, canvasShadow.height);
  canvasContextShadow.drawImage(canvas, 0, 0);
}

function ResetCanvas() {
  canvasContext.clearRect(0, 0, canvas.width, canvas.height);
  canvasContext.drawImage(canvasShadow, 0, 0);
}
//Events
var pos = {
  x: 0,
  y: 0
};

var array = {
    x: [],
    y: []
}
img = new Image();
img.src = "./noun.svg"
img.onload = function(){
    console.log("What you want?");
    canvasContext.drawImage(img,0,0);
}
path = new Path2D("M70.8,40.6c-13-2.3-27,1.1-37.5,9.2c1.3-3.4,2.5-7,2.1-10.6c-0.3-3.6-2.5-7.3-6-8.3c-1.2-0.3-2.7-0.3-3.7,0.5  c-1,0.8-1.4,2.5-0.5,3.4c0.8,0.8,2.2,0.8,3.1,0.1c0.9-0.6,1.5-1.6,2-2.7c1.3-2.9,1.9-6.2,1.8-9.4c-0.5,2.3-2.4,4.1-4.4,5.3  s-4.3,2-6.4,3.1C15,34.7,10.7,41.6,10.3,48.9c1,0.4,2.2,0.2,3-0.6s0.8-2.2,0.2-3.1c-1.8-0.2-3.5,1.9-3.2,3.8  c0.3,1.8,2.1,3.1,3.9,3.7c1.8,0.5,3.7,0.4,5.6,0.4c1.9-0.1,3.8,0,5.5,0.7c3.4,1.5,4.9,5.6,5.1,9.3c0.4,6.9-2.4,13.5-5.2,19.8  c-0.3-1.6-2.1-2.7-3.7-2.3c-1.6,0.4-2.6,2.2-2.2,3.7c0.7,2.5,4.3,3,6.5,1.6c2.2-1.4,3.3-3.9,4.6-6.2c3.5-6.4,8.8-11.8,15.4-14.8  s14.6-3.1,21,0.2s11,10.4,10.6,17.6c-0.7-2.2-4.4-2.1-5.3,0c-0.9,2.1,0.7,4,3,4.5c2.2,0.5,4.6-0.1,5.9-2c1.3-1.9,1.7-4.2,1.8-6.5  c0.1-2.3-0.1-4.6,0.1-6.9c0.4-3.6,3.2-7.1,4.4-10.6c1.2-3.4,1.5-7,1.1-10.6c-0.4-3.6-3.3-7.2-6.8-8.3c-1.2-0.4-2.6-0.5-3.8,0.1  c-1.2,0.6-2,1.8-1.8,3.1c0.2,1.8,2.4,2.9,4.2,2.5s3.2-1.7,4.4-3.1c5.6-6.6,5.4-10.3,0.7-17.4c-3.7-5.6-3.4-14.5,5.1-15.3")
var m = document.createElementNS("http://www.w3.org/2000/svg", "svg").createSVGMatrix()
const t = m.scale(5)
p = new Path2D()
p.addPath(path,t);
canvasContext.stroke(p);

document.addEventListener('mousemove', draw);
document.addEventListener('mousedown', setPosition);
document.addEventListener('mouseenter', setPosition);
document.getElementById("reset").addEventListener('click', ResetCanvas);
document.getElementById("save").addEventListener('click', SaveCanvas);
function setPosition(e) {
  var rect = canvas.getBoundingClientRect();
  pos.x = e.clientX - rect.left;
  pos.y = e.clientY - rect.top;
}

function draw(e) {
  if (e.buttons !== 1)
    return;
  canvasContext.beginPath();
  canvasContext.lineWidth = 5;
  canvasContext.lineCap = 'round';
  canvasContext.strokeStyle = '#c0392b';
  canvasContext.moveTo(pos.x, pos.y);
  array.x.push(pos.x);
  array.y.push(pos.y);
  setPosition(e);
  canvasContext.lineTo(pos.x, pos.y);
  canvasContext.stroke();
}

