var _host = "/zhongyejituan/static/sample/";
/* 加载器：注意文件排序决定加载顺序*/
_load([
	"css/bootstrap.min.css",
	"fonts/font-awesome/css/font-awesome.min.css",
	"css/bootstrap-select.min.css",
	"css/bootstrapValidator.min.css",
	"js/tmpl.min.js",
	"js/jquery.min.js",
	// "https://cdn.bootcss.com/jquery.nicescroll/3.7.6/jquery.nicescroll.min.js",
	"js/bootstrap.min.js",
	"js/director.min.js",
	"js/moment.min.js",
	"js/layer.js",
	"js/bootstrap-paginator.min.js",
	"js/bootstrap-select.min.js",
	"js/bootstrapValidator.min.js",
	"js/ping.min.js",
	"css/common.css",
	"js/common.js",
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
