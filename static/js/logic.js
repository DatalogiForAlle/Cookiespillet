function makeDiv() {
  var divsize = ((Math.random() * 100) + 150).toFixed();
  var posx = (Math.random() * ($(document).width() - divsize)).toFixed();
  var posy = (Math.random() * ($(document).height() - divsize)).toFixed();

  var color = '#' + Math.round(0xffffff * Math.random()).toString(16);
  $newdiv = $('<div/>').css({
    'width': divsize + 'px',
    'height': divsize + 'px',
    'background-color': color
  });
  $newdiv.html('<button class="btn">Ja til cookies</button>&nbsp;<button class="btn">Nej til cookies</button>')
  $newdiv.css({
    'position': 'absolute',
    'left': posx + 'px',
    'top': posy + 'px',
    'display': 'none',
  }).appendTo('body').fadeIn(100);


}


(function myLoop(i) {
  setTimeout(function () {
    makeDiv() //  your code here
    if (--i) myLoop(i);   //  decrement i and call myLoop again if i > 0
  }, 50)
})(35);



$(document).on('click', '.btn', function () {
  console.log($(this).parent().hide())
})
