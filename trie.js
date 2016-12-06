var trie = (function() {
  this.leaf = false;
  this.next = {}
  var add_item = function(node, str) {
    for (var i = 0; i < str.length; i++) {
      var k = str[i];
      if (!node.next[k])
        node.next[k] = new Node()
      node = node.next[k]
    }
    node.leaf = true
  }
  var dfs = function(node, str) {
    if (node.leaf)
      console.log(str)
    for (var i in node.next) {
      var s = str + i;
      this.dfs(node.next[i], s)
    }
  }
  var autocomplete = function(node, str) {
    var s = ""
    for (var i = 0; i < str.length; i++) {
      var k = str[i]
      if (node.next[k])
        node = node.next[k]
      else
        return "not found"
      s += str[i]
    }
    this.dfs(node, s)
  }
  var Node = function() {
    this.leaf = false;
    this.next = {}
  }
  return {
    autocomplete: autocomplete,
    Node: Node,
    add_item: add_item,
    dfs: dfs
  }
});
var list = [
  'sin',
  'singh',
  'sign',
  'sinus',
  'sit',
  'silly',
  'side',
  'son',
  'soda',
  'sauce',
  'sand',
  'soap',
  'sar',
  'solo',
  'sour',
  'sun',
  'sure',
  'and',
  'ask',
  'animal',
  'an',
  'ant',
  'aunt',
]
var x = trie()
node = new x.Node()
list.forEach(function(s) {
  x.add_item(node, s);
});
x.autocomplete(node, "si")
