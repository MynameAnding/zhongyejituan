var _router = routerSet({});
var _admin = JSON.parse(sessionStorage.getItem("admin") || "{}");
$(function() {
	// if ($.isEmptyObject(_admin)) {
	// 	window.location.href = "#page/admin/login.html";
	// } else if (getHash() == "") {
	// 	$.when($(".authority").html(tmpl("authority-list", _admin))).done(function() {
	// 		$(".authority>li:first>a")[0].click();
	// 	});
	// }
	// $("#userName").text(_admin.login_name);
});
/* 路由绑定 */
function routerSet(routes) {
	var show = function(page, file, html) {
		if ($("#myModal").length > 0) {
			getPage("#myModal", page + "/" + file + "/" + html, function() {
				$("#myModal").modal('show');
			});
		} else {
			history.go(-1);
		}
	};
	var login = function() {
		getPage("#login", "page/admin/login.html", function() {
			$("#login").modal('show');
		});
	};
	var _routes = {
		'show/:page/:file/:html': show,
		'page/admin/login.html': login
	};
	_router && _router.destroy();
	routes = $.extend({}, _routes, routes);
	_router = Router(routes).configure({
		on: function() {
			// getPage(getHash()); //默认回调
		},
		notfound: function() {
			if (getHash()) {
				getPage(".page-html", getHash(), function() {
					$.when($(".authority").html(tmpl("authority-list", _admin))).done(function() {
						// var href = getHash().replace(".html","");
						var hash = getHash();
						hash = hash.substr(0, hash.lastIndexOf(".html"));
						if ($(".sidebar-menu a[href*='" + hash + "']").length > 0) {
							$(".sidebar-menu a[href*='" + hash + "']").parent().addClass("click").siblings().removeClass("click");
						}
					});
					$(".page-html-show").removeClass("page-html-show");
					$(".modal-open").removeClass("modal-open");
				});
			} else {
				history.go(-1); //错误回调
			}
		}
	}).init();
	return _router;
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
/* 权限枚举 */
var roles = ["课程管理", "用户管理", "订单管理", "反馈消息", "数据统计", "管理员/权限", "习题管理", "广告管理"]

function setRoles(rolenum) {
	for (var i = 0, l = roles.length; i < l; i++) {
		rolenum = rolenum.replace(i, roles[i]);
	}
	return rolenum;
}
/* 删除方法 */
function isDelete(id, url) {
	swal({
			title: "确定删除吗？",
			text: "你将无法恢复该数据！",
			type: "warning",
			showCancelButton: true,
			confirmButtonColor: "#DD6B55",
			confirmButtonText: "确定",
			cancelButtonText: "取消",
			closeOnConfirm: false
		},
		function() {
			$.$ajax({
				type: "post",
				url: _host + url,
				data: {
					id: id
				},
				success: function(res) {
					if (res.statusCode == 0) {
						getList();
						showOk();
					} else {
						swal("操作失败", "", "error");
					}
				}
			});
		});
}
/* 书籍绑定 */
function setBooks(tmp, tmpunit, tmplesson, book_id, unit_id, curriculum_id) {
	if (!tmp) return;
	$.$ajax({
		url: _host + "index.php/yn/book/getBooks",
		success: function(res) {
			if (res.statuscode == '0') {
				$("#book").html(tmpl(tmp, res)).selectpicker("refresh");
				$("#book").selectpicker("val", book_id);
				setUnits(book_id || res.result[0].book_id, tmpunit, tmplesson, unit_id, curriculum_id);
			}
		}
	});
}
/* 单元绑定 */
function setUnits(id, tmp, tmplesson, unit_id, curriculum_id) {
	if (!tmp) return;
	$.$ajax({
		url: _host + "index.php/yn/unit/getUnits",
		data: {
			id: id
		},
		success: function(res) {
			if (res.statuscode == '0' || res.statusCode == '0') {
				$("#unit").html(tmpl(tmp, res)).selectpicker("refresh");
				$("#unit").selectpicker("val", unit_id);
				setLessons(unit_id || res.result[0].unit_id, tmplesson, curriculum_id);
			}
		}
	});
}
/* 课程绑定 */
function setLessons(id, tmp, curriculum_id) {
	if (!tmp) return;
	$.$ajax({
		url: _host + "index.php/yn/curriculum/getCurriculums",
		data: {
			id: id
		},
		success: function(res) {
			if (res.statuscode == '0' || res.statusCode == '0') {
				$("#lesson").html(tmpl(tmp, res)).selectpicker("refresh");
				$("#lesson").selectpicker("val", curriculum_id);
			}
		}
	});
}
/* 多级联动 */
function setOption(dom, pid, id) {
	if (!dom) return;
	$.$ajax({
		url: _host + "index.php/yn/" + dom + "/getList",
		data: {
			id: pid || ""
		},
		success: function(res) {
			if (res.statuscode == '0') {
				var htmlStr = ""
				for (var i = 0; i < res.result.length; i++) {
					htmlStr += tmpl("<option value=\"{%=o['id']%}\">第{%=o[\"name\"]%}{%=o[\"unit\"]%}</option>", res.result[i]);
				}
				$("#" + dom).html(htmlStr).selectpicker("refresh");
				$("#" + dom).selectpicker("val", id || res.result[0].id).trigger("change");
			}
		}
	});
}
