# 附录：物景

## 道具
&emsp;角色在0级时拥有150点宠爱。她可以获取任何稀有度不超过N的道具，只要她的宠爱能够承受这些道具的恶意。在GM许可的情况下，角色也可以获取稀有度为R或更高的道具。

### 恶意
&emsp;大多数道具都拥有恶意，用于表示获取它所占用的宠爱。恶意为「—」的道具无法通过占用宠爱来获取。  
&emsp;角色携带的所有道具的恶意之和，不能超过她的宠爱。当恶意超过宠爱时，角色无法获得任何恶意不为「—」的道具。并且，角色无法使用造成超出的那部分恶意的道具，在判断其他效果时，视角色未携带那些道具。

### 道具级别
&emsp;每件道具都拥有级别，用于表示道具的科技和魔法含量。未标注级别的道具，级别默认为0。角色可以使用任何级别的道具，但是无法制作级别超过 `LV/2` 的道具。

### 携带道具
&emsp;携带道具的方法分为2种：装备与受纳。道具只能被装备在拥有「装备栏」的部位上。当部位<欠损>时，装备其中的所有道具都会掉落至原地。丢弃1件装备中的道具、改变装备中的1件道具的装备栏、或交换装备中的2件道具，需要使用【交互】或【驱使】动作。  
&emsp;存放在被装备的容器中的道具，则属于被受纳的道具。装备一件被受纳的道具，需要使用【驱使】动作。

<hr>

### 武器
&emsp;对于不了解魔法的角色而言，一把趁手的武器是能否在搏杀中生存下来的关键。武器的类型一共分为以下几种。
- **搏击**：这类武器着重于近身缠斗，主要通过猛击和施加压力造成伤害，如棍棒、拳脚和战锤等。
- **刀剑**：这类武器以锋利的刀刃作为主要攻击部件，如弯刀、长剑、匕首等。
- **枪戟**：这类武器着重于远距离的挥砍和突刺，如长矛、骑枪、战戟等。
- **软兵**：这类武器使用柔软材料制作，主要通过摆动和甩打进行攻击，如鞭子、链枷和流星锤等。
- **弓弩**：这类武器利用弹力发射弹药，如长弓、手弩和石弩等。
- **铳械**：这类武器利用推力发射弹药，如手枪、火炮和火箭筒等。
- **爆破**：这类武器会产生剧烈的爆炸，如炸药、手榴弹和飞弹等。
- **毒剂**：这类武器利用有毒物质作为攻击手段，如毒素、毒气和病毒等。
- **奇门**：这类武器无法被分入上述中的任何一类。每个奇门武器都视为单独的一种武器类型。

#### 武器标签
- **近战**：这件武器主要用于近身格斗。不过也可以投掷出去以进行远程攻击，此时射程视为「0~1'」，并附加 `应急` 标签。
- **远程**：这件武器主要用于远距射击。不过也可以作为近战武器敲打别人，此时射程视为「0」，并附加 `应急` 标签。
- **投掷**：这件武器既可用于近身格斗，也适合投掷出去进行远程攻击。这件武器的射程表述为「[近战射程]/[远程射程]」。
- **重型**：这件武器十分沉重，通过此武器执行的动作，需要额外消耗1点AP。
- **轻型**：这件武器十分轻巧，通过此武器执行的动作，产生的连击减值减少1点。
- **精妙**：通过此武器发起的近战攻击，可以将「灵巧」作为攻击技能。
- **附着**：这件武器不会占用装备栏，因此也不会被缴械。若装备此武器的装备栏被占用，则无法通过此武器执行动作。
- **长柄**：这件武器拥有长长的握柄，可以攻击到远处的敌人，但也不擅长应对较近的敌人。此武器的近战射程+1。
- **装填**：这件武器在每次发起攻击时都会消耗1发弹药，若弹药不足则无法发起攻击。所能容纳的弹药数量上限被称为「弹容」。角色需要使用【驱使】重装弹药，可以一次性重装所有被消耗的弹药。

#### 武器需求
&emsp;所有武器都会对一项或多项属性的数值拥有需求。角色每有1项未满足需求的属性，她在使用那件武器执行动作时，ATK就会受到2点内在减值，这些减值会自相叠加。如果角色未满足对体能属性的需求，武器的DP还会再受到1点减值。

#### 应急武器
&emsp;一些事物并非专门作为武器而设计。这些事物依然可以作为武器使用，不过会因此获得 `应急` 标签。  
&emsp;无论武器的类型是什么，角色对 `应急` 武器的熟练度总是视为0，并且DP-1 (最低1)。

### 设计武器
&emsp;角色可以根据以下流程自行设计武器。设计完毕的武器，恶意不能超过100点。
- **第一步：基础特性**  
  武器的恶意基础为0点，并具有以下特性。  
  ▼ **伤害**  
  ｜武器的基础DP为1点，从 `冲击` 、 `切割` 、 `穿刺` 中选择1项作为伤害类型。  
  ▼ **射程**  
  ｜从 `近战` 、 `远程` 、 `投掷` 中选择1项附加在武器之上。近战武器的射程基础为「0」，远程武器的射程基础为「0~4'」，投掷武器的射程基础为「0/0~1'」。
  <hr>
- **第二步：武器类型**  
  选择1项奇门之外的武器类型，作为该武器的类型。一部分武器类型拥有特殊的设计规则。  
  ▼ **枪戟**  
  ｜枪戟武器必须附加强化特性 `长柄` 。  
  ▼ **铳械**  
  ｜铳械武器必须附加强化特性 `装填` 。  
  ▼ **毒剂**  
  ｜毒剂武器的恶意增加5点，伤害类型必须从 `冲击` 、 `切割` 、 `穿刺` 之外的其他选项中选择。如果选择精神伤害，则恶意再增加5点。
  <hr>
- **第三步：属性需求**  
  武器对属性的需求基础为「次等体能」与「次等协调」。铳械、爆破、与毒剂武器还具有「次等智慧」的需求。
  <hr>
- **第四步：强化特性**  
  角色可以为武器附加下列强化特性。若无特别说明，不能重复附加相同的强化特性。  
  ▼ **增加伤害 (恶意 10)**  
  ｜武器的DP增加1点。这项强化特性可以附加3次。  
  ｜第二次附加时，如果是近战武器或投掷武器，则对体能的需求提升至「标准体能」；如果是远程武器，则对协调的需求提升至「标准协调」。如果是铳械、爆破、或毒剂武器，则对智慧的需求还会提上至「标准协调」。  
  ｜第三次附加时，对上述属性中最高的需求提升至「高等阶层」，对其他属性的需求提升至「标准阶层」。  
  ▼ **额外伤害类型 (恶意 5+)**  
  ｜从可以选择的伤害类型中选择1项还未选择的伤害类型。武器每次造成伤害前，角色可以将所选的伤害类型，作为这次伤害的伤害类型。如果选择精神伤害，则恶意再增加5点。  
  ▼ **混合伤害类型 (恶意 20+)**  
  ｜从可以选择的伤害类型中选择1项还未选择的伤害类型。武器会造成所选伤害类型与原本伤害类型的混合伤害。如果选择精神伤害，则恶意再增加10点。  
  ▼ **长柄 (恶意 10)**  
  ｜武器获得 `长柄` 标签。  
  ▼ **装填 (恶意 -10)**  
  ｜武器获得 `装填` 标签。弹容基础为1。  
  ▼ ** (恶意 )**  
  ｜  
  ▼ ** (恶意 )**  
  ｜  

<hr>

### 防具
&emsp;装备防具可以保护角色免受伤害。防具的类型一共分为以下几种。装备防具时，闪避防御将使用角色对防具的熟练度，而非闪避防御原本的熟练度。
- **轻装**：装备轻装不会改变闪避防御的防御技能。
- **重装**：装备重装的角色需要将「运动」取代「灵巧」作为闪避防御的防御技能。

#### 防具标签

<hr>

### 道具列表

#### 道具格式模板

##### 名称　　　　　　｜　级别
———————————————————————————————<br>
`标签` `标签` `标签`<br>
**恶意**：道具所有规格的恶意<br>
**需求**：道具生效所必须满足的需求条件<br>
**执行**：道具发动的时机　｜　**消耗**：使用道具所必须付出的代价<br>
**时效**：道具生效的时长　｜　**频率**：道具的使用次数上限<br>
**射程**：道具的射程距离　｜　**范围**：道具的效果范围<br>
———————————————————————————————<br>
_/ *道具的效果描述。*<br>
道具的效果内容。<br>
— <span class=V>v</span> **规格** &nbsp;——————————————————————————<br>
道具在不同规格下的效果。<br>
— <span class=V>v</span> **制作** &nbsp;——————————————————————————<br>
制作道具的特殊条件。

> ▼ **个性化**  
｜获取一个新的道具时，角色可以随意修改道具的名称和描述。这不会改变道具的效果，也不会影响道具与其他效果的联动。

<hr>

#### 武器

##### 短棒
———————————————————————————————<br>
`搏击` `近战`<br>
**恶意**：0<br>
**需求**：次等体能、次等协调<br>
**射程**：0<br>
———————————————————————————————<br>
_/ *这是一块结实的木头，经过打磨的形状专门用于敲击敌人。*<br>
造成1点 `冲击` 伤害。

##### 锤矛
———————————————————————————————<br>
`搏击` `近战`<br>
**恶意**：4<br>
**需求**：标准体能、次等协调<br>
**射程**：0<br>
———————————————————————————————<br>
_/ *这种武器呈棍状或矛状，一端带有很重的负重，造成的强力打击给盔甲留下凹痕。*<br>
造成1点 `冲击` 或 `穿刺` 伤害。

##### 匕首
———————————————————————————————<br>
`刀剑` `投掷` `轻型` `精妙`<br>
**恶意**：2<br>
**需求**：次等体能、次等协调<br>
**射程**：0/0~4<br>
———————————————————————————————<br>
_/ *这种小型有刃的武器可以在近战中刺伤敌人。也可以用来投掷。*<br>
造成1点 `切割` 或 `穿刺` 伤害。

<hr>

#### 防具