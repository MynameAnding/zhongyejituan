var _host = "/jsayClient/";
/* 加载器：注意文件排序决定加载顺序*/
_load([
	"js/config.js",
	"css/admin.css"
])

function _load(list) {
	for (var item in list) {
		if (list[item].indexOf(".js") > -1) {
			document.write('<script src="' + _host + list[item] + '"></script>');
		} else if (list[item].indexOf(".css") > -1) {
			document.write('<link href="' + _host + list[item] + '" rel="stylesheet">');
		}
	}
}
