$("#sample_idPro").editable({
  type: "text",                //编辑框的类型。支持text|textarea|select|date|checklist等
  title: "用户名",              //编辑框的标题
  validate: function (value) { //字段验证
    if (!$.trim(value)) {
      return '不能为空';
    }
  }
});

$("#type").editable({
  type: "select",                //编辑框的类型。支持text|textarea|select|date|checklist等
  title: "委托类型",              //编辑框的标题
  // validate: function (value) { //字段验证
  //   if (!$.trim(value)) {
  //     return '不能为空';
  //   }
  // }
  source:[{value:"1",text:"研发部"},{value:"2",text:"销售部"},{value:"3",text:"行政部"}]
})
$("#date").editable({
  type:"date",
  title:"委托日期"
})
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()
$("#sample_idPro").editable()