window.onload = function() {
  var elements = document.getElementsByClassName('show');
  for (var i = 0; i < elements.length; i++) {
    var element = elements[i];
    if (element.id === '绝技') {
      element.innerText = "每一刻最多只能宣言1次 [绝技] 动作";
    } else if (element.id === '起手') {
      element.innerText = "只能在尚未宣言过 [移动]、[攻击] 或 [起手] 动作的刻度中使用";
    }
  }
};