window.onload = function() {
  var 绝技 = document.getElementById('绝技');
  for (var i = 0; i < 绝技.length; i++) {
    绝技[i].innerText = "每一刻最多只能宣言1次 [绝技] 动作";
  }
  var 起手 = document.getElementById('起手');
  for (var i = 0; i < 起手.length; i++) {
    起手[i].innerText = "只能在尚未宣言过 [移动]、[攻击] 或 [起手] 动作的刻度中使用";
  }
}; 