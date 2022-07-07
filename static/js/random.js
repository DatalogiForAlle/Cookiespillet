const positions = [" TL", " TM", " TR", " ML", " MM", " MR", " BL", " BM", " BR"];
const images = [" img1", " img2", " img3", " img4", " img5", " img6", " img7", " img8", " img9", " img10", " img11", " img12", " img13",];

const random = Math.floor(Math.random() * images.length);
const random2 = Math.floor(Math.random() * positions.length);

document.getElementById("image").className += images[random];
document.getElementById("position").className += positions[random2];