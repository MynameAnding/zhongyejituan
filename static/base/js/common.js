var _host = "/jsayClient/";
var _admin = JSON.parse(sessionStorage.getItem("admin")||"{}");
/* ajax封装 */
$.$ajax = function(setting) {
	return $.ajax({
		type: setting.type || "POST",
		data: $.extend({}, setting.data, {}) || "{}",
		url: setting.url || "",
		dataType: setting.dataType || "json",
		success: function(d) {
			setting.success && setting.success(d);
		},
		error: function(e) {
			setting.error && setting.error(e);
		}
	});
};
/* form表单转json对象 */
$.fn.serializeObject = function() {
	var o = {};
	$.each(this.serializeArray(), function() {
		if (o[this.name] !== undefined) {
			if (!o[this.name].push) {
				o[this.name] = [o[this.name]];
			}
			o[this.name].push(this.value || '');
		} else {
			o[this.name] = this.value || '';
		}
	});
	return o;
};
/* 获取路由hash值 */
function getHash() {
	return window.location.hash.slice(1);
}
/* 获取参数 */
function getQueryString(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
	var r = window.location.search.substr(1).match(reg);
	if (r != null) return unescape(r[2]);
	return null;
}
/* 获取hash参数 */
function getHashQuery(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
	var r = window.location.hash.substr(window.location.hash.indexOf("?") + 1).match(reg);
	if (r != null) return unescape(r[2]);
	return null;
}
/* 上传绑定 */
function bindUpload(obj) {
	return new plupload.Uploader($.extend({}, {
		runtimes: 'html5,flash,silverlight,html4',
		flash_swf_url: 'js/Moxie.swf',
		silverlight_xap_url: 'js/Moxie.xap',
		multi_selection: false,
		chunk_size: '1mb',
		max_retries: 3,
		init: {
			BeforeUpload: function(up, file) {},
			UploadProgress: function(up, file) {},
			Error: function(up, err) {},
			FileUploaded: function(up, file, result) {},
			UploadComplete: function(up, file) {}
		}
	}, obj)).init();
}
/* 询问弹窗 */
layer.confirmWin = function(word, btn, ok, no) {
	return layer.confirm(word || "是否确定该操作!", {
		btn: btn || ["确定", "取消"]
	}, function() {
		if (typeof ok == "function") {
			ok();
		}
	}, function() {
		if (typeof no == "function") {
			no();
		}
	});
}
/* 确认弹窗 */
layer.info = function(word, callback) {
	return layer.alert(word || "是否确定该操作!", {
		time: 5000,
		icon: 0
	}, function() {
		if (typeof callback == "function") {
			callback();
		}
	});
}
/* 成功弹窗 */
layer.success = function(word, callback) {
	return layer.msg(word || "操作成功!", {
		icon: 1
	}, function() {
		if (typeof callback == "function") {
			callback();
		}
	});
}
/* 错误弹窗 */
layer.error = function(word, callback) {
	return layer.msg(word || "操作失败!", {
		icon: 2
	}, function() {
		if (typeof callback == "function") {
			callback();
		}
	});
}
/* 客户端自定义弹窗 */
layer.windows = function(url, size) {
	return layer.open({
		type: 1,
		title: 0,
		closeBtn: 0,
		area: size || ["500px", "300px"],
		content: '<iframe src="' + url + '" width="100%" height="100%" frameborder=0 ></iframe>' +
			'<button type="button" class="close-btn" onclick="layer.closeNow()"><i class="fa fa-close"></i></button>'
	});
}
/* 管理端自定义弹窗 */
layer.Windows = function(url, size, callback) {
	return layer.open({
		type: 1,
		title: 0,
		closeBtn: 1,
		area: size || ["500px", "300px"],
		content: '<iframe src="' + url + '" width="100%" height="100%" frameborder=0 scrolling="no"></iframe>',
		end: function() {
			if (typeof callback == "function") {
				callback();
			}
		}
	});
}
/* 管理端自定义弹窗 */
layer.full = function(url, callback) {
	return layer.open({
		type: 2,
		content: url,
		area: ['100%', '100%'],
		title: 0,
		closeBtn: 0,
		end: function() {
			if (typeof callback == "function") {
				callback();
			}
		}
	});
}
/* 动态调整开窗大小 */
layer.resize = function(height) {
	$("#layui-layer" + layer.index).height(height)
	$("#layui-layer" + layer.index + ">.layui-layer-content").height(height)
}
/* 关闭当前窗口 */
layer.closeNow = function() {
	return layer.close(layer.index)
}
/* 权限枚举 */
var roles = ["课程管理", "活动设置", "园所配置", "用户行为", "园所管理", "系统设置"]

function setRoles(rolenum) {
	for (var i = 0, l = roles.length; i < l; i++) {
		rolenum = rolenum.replace(i, roles[i]);
	}
	return rolenum;
}
// 时间控件汉化
var locale = {
	"format": 'YYYY/MM/DD',
	"separator": " -- ",
	"applyLabel": "确定",
	"cancelLabel": "取消",
	"fromLabel": "起始时间",
	"toLabel": "结束时间'",
	"customRangeLabel": "自定义",
	"weekLabel": "W",
	"daysOfWeek": ["日", "一", "二", "三", "四", "五", "六"],
	"monthNames": ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
	"firstDay": 1
};
/* 网络检测 */
function setNet() {
	new Ping().ping(_host, function(err, data) {
		if (!err) sessionStorage.setItem("online", 1)
	});
	window.addEventListener("online", function() {
		sessionStorage.setItem("online", 1)
	})
	window.addEventListener("offline", function() {
		sessionStorage.removeItem("online")
	})
}

function getNet() {
	return sessionStorage.getItem("online")
}

/* 文件类型判断 */
function getFileType(file) {
	if ((/\.jpg$|\.jpeg$|\.png$|\.gif$/i).test(file)) {
		return "picture";
	}
	if ((/\.mp3$|\.wav$/i).test(file)) {
		return "audio";
	}
	if ((/\.mp4$|\.webm$|\.ogg$|\.avi$|\.wmv$|\.mov$/i).test(file)) {
		return "video";
	}
	if ((/\.doc$|\.docx$|\.xls$|\.xlsx$|\.ppt$|\.pptx$/i).test(file)) {
		return "office";
	}
	if ((/\.zip$|\.swf$|\.flv$/i).test(file)) {
		return "zip";
	}
	return "files";
}
