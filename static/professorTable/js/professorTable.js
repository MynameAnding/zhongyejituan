var dict = {
    'name': "试样编号",
    "danwei": "钢号级别",
    "zhengzhimianmao": "规格mm",
    "zhiwu": "面积mm²",
    "zhicheng": "屈服\n负荷kN Fp0.2",
    "shenfenzhenghao": "屈服\n强度 \nMPa Rp0.2",
    "lianxidianhua": "最大负荷 kN Rm",
    "kechengmingcheng": "抗拉强度 MPa Rm",
    "kaihuhang": "原始标距mm",
    "kahao": "断后标距 mm",
    "shehuijianzhi": "伸长率%",
    "hezuoqingkuang": "最大力原始标距 mm",
    "zhengzhibiaoxian": "最大力断后标距 mm",
    "shoukejilu": "最大力总延伸率 %",
    "labels": "强屈比",
    "jianjie": "屈屈比",
};
function hello(){
    var text = $("button[id='btn_user']").html();
    alert("你好"+text);
}
$('#ProfessorTable').bootstrapTable({
    url: '/LoadData/',
    responseHandler: 'HandleData',

    method: 'post',
    showColumns: true,
    showRefresh: true,
    clickToSelect: true,
    maintainSelected: true,
    detailView: false,
    search: true,
    searchAlign: 'left',
    toolbar: '#toolbar',
    toolbarAlign: 'left',
    undefinedText: '',
    showFooter: false,
    //onlyInfoPagination:true,
    minimumCountColumns:6,
    paginationVAlign:'top',

    uniqueId: 'ID',
    pagination: true, // 是否分页
    pageSize:20,
    // pageList: [5, 10, 15, 20],
    // showPaginationSwitch: true,
    smartDisplay: true,
    showExport: true,  //是否显示导出按钮
    buttonsAlign: "right",  //按钮位置
    exportTypes: ['excel'],  //导出文件类型
    exportDataType: 'selected',//basic', 'all', 'selected'.
    exportOptions: {
        ignoreColumn: [0, 18],  //忽略某一列的索引
        fileName: '专家信息',  //文件名称设置
        worksheetName: 'sheet1',  //表格工作区名称
        tableName: '专家信息',
        excelstyles: ['background-color', 'color', 'font-size', 'font-weight', 'border-top'],
    },
    locale: 'zh-CN',
    columns: [
        {
            checkbox: true,
        },
        {
            field: 'ID',
            title: '试样编号',
            align:'center',
            valign:'center',
            max_width:30,
            sortable:true,

        },
        {
            field: 'name',
            title: '钢号级别',
            align:'center',
            width:"1em",
            valign:'center',

        },
        {
            field: 'danwei',
            title: '规格mm',
            align:'center',
            width:"1em",
            valign:'center',

        },
        {
            field: 'zhengzhimianmao',
            title: '面积 mm²',
            align:'center',
            valign:'center',
            width:"1em",
        },
        {
            field: 'zhiwu',
            title: '屈服负荷kNFp0.2',
            align: 'center',
            width:"1em",
            valign:'center',

        },
        {
            field: 'zhicheng',
            title: '屈服强度MPaRp0.2',
            maxHeight:'5em',
            align: 'center',
            width:"1em",
            valign:'center',

        },
        {
            field: 'shenfenzhenghao',
            title: '最大负荷kNFm',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'lianxidianhua',
            title: '抗拉强度MPaRm',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'kechengmingcheng',
            title: '原始标距mm',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'kaihuhang',
            title: '断后标距mm',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'kahao',
            title: '伸长率%',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'shehuijianzhi',
            title: '最大力原始标距mm',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'labels',
            title: '最大力断后标距mm',
            align: 'center',
            valign:'center',
            width:"1em",

        },

        {
            field: 'hezuoqingkuang',
            title: '最大力总延伸率%',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'zhengzhibiaoxian',
            title: '强屈比',
            align: 'center',
            valign:'center',
            width:"1em",

        },
        {
            field: 'shoukejilu',
            title: '屈屈比',
            align: 'center',
            valign:'center',

        },
    ]
});

function upImages(id,name) {
    // console.info(id,name);
    layx.iframe('localsite', '上传'+name+'专家的照片', '/upImages/'+id);
}

function createProf() {
    layx.html('htmlstr', '添加专家信息', layx.multiLine(
        '<form action="./createProf/" method="POST"  ><input type="hidden" name="id"><table id="CreateProf" class="table-hover table-striped"></table></form>'
    ));
    var data = [];
    for (var key in dict) {
        var r = 2;
        if (key !== "photos" && key !== "labels") {
            var d = {
                "biaoqian": dict[key] + ':',
                "neirong": '<textarea style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="' + r + '" cols=27></textarea>'
            };
            data.push(d);
        }
        if (key === "labels") {
            var d = {
                "biaoqian": dict[key] + ':',
                "neirong": '<textarea placeholder="如有多个标签请用任意的符号隔开" style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="' + r + '" cols=27></textarea>'
            };
            data.push(d);
        }
    }
    // var neirong = '';
    // neirong += '<button value="上传照片" class="btn btn-primary" onclick="upImages()"></button>';
    // data.push({"biaoqian": "照片:", "neirong": neirong});
    data.push({"biaoqian": "", "neirong": '<button class="btn btn-primary btn-sm"  type="submit">提交</button>'});
    $("#CreateProf").bootstrapTable({
        data: data,
        columns: [{
            field: 'biaoqian',
            title: ''
        }, {
            field: 'neirong',
            title: ''
        }]
    });
}

function CheckProf(){
    layx.iframe('radiu-style', '审核上传的专家信息', '/checkProf/', {
        style: layx.multiLine(function () {
            /*
        #layx-radiu-style{
            border-radius:4px;
            -webkit-border-radius:4px;
            -moz-border-radius:4px;
            -ms-border-radius:4px;
        }
        icon:false

        #layx-radiu-style .layx-window-icon{
            color:#f00;
        }
        */
        })
    });
}
function userAdmin(){
    layx.iframe('radiu-style', '管理用户信息', '/userAdmin/', {
        style: layx.multiLine(function () {
            /*
        #layx-radiu-style{
            border-radius:4px;
            -webkit-border-radius:4px;
            -moz-border-radius:4px;
            -ms-border-radius:4px;
        }
        icon:false

        #layx-radiu-style .layx-window-icon{
            color:#f00;
        }
        */
        })
    });
}
function updateProf(id) {
    var row = $('#ProfessorTable').bootstrapTable('getRowByUniqueId', id);//行的数据
    layx.html('htmlstr', '修改专家信息', layx.multiLine(
        '<form action="./updateProf/" method="POST"><input type="hidden" name="id" value="' + id + '"><table id="updateTable" class = "table-striped"></table></form>'
    ));
    var data = [];
    for (var key in dict) {
        var r = 2;
        if (key !== "photos" && key !== "labels") {
            if (row[key] !== null) {
                r = Math.ceil(row[key].length / 30);
            }
            var d = {
                "biaoqian": dict[key] + ':',
                "neirong": '<textarea style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="' + r + '" cols=27>' + row[key] + '</textarea>'
            };
            data.push(d);
        }
        if (key === "labels") {
            if (row[key] !== null) {
                r = Math.ceil(row[key].length / 30);
            }
            var d = {
                "biaoqian": dict[key] + ':',
                "neirong": '<textarea placeholder="如有多个标签请用括号内的符号（，）隔开" style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="' + r + '" cols=27>' + row[key] + '</textarea>'
            };
            data.push(d);
        }
    }
    // var neirong = '';
    // for (var url in row['photos']) {
    //     neirong += '<img src="' + url + '" width="100px" height="100px"/>'
    // }
    // data.push({"biaoqian": "照片:", "neirong": neirong});
    data.push({"biaoqian": "", "neirong": '<button class="btn btn-primary btn-sm"  type="submit">提交</button>'});
    $("#updateTable").bootstrapTable({
        data: data,
        uniqueId: "MENU_ID",
        columns: [{
            field: 'biaoqian',
            title: ''
        }, {
            field: 'neirong',
            title: ''
        }]
    });
}

function HandleData(res) {
    // console.info(res);
    return res;
}


function showDetail(index, row, $detail) {
    var data = [];
    var ind = 0;
    var d = {}
    for (var key in dict) {
        if (key !== "photos" && key !== 'jianjie') {
            if (row[key] === null) {
                r = 1;
            }
            else {
                var r = Math.ceil(row[key].length / 50);
            }
            if (ind % 2 === 0) {
                d = {};
                d["biaoqian1"] = dict[key] + ':';
                d["neirong1"] = '<textarea  readonly="readonly" style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="' + r + '" cols=27>' + row[key] + '</textarea>';
            }
            else {
                d["biaoqian2"] = dict[key] + ':';
                d["neirong2"] = '<textarea  readonly="readonly" style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="' + r + '" cols=27>' + row[key] + '</textarea>';
                data.push(d);
            }
        }
        ind += 1
    }
    data.push(d);
    var neirong = '';
    // console.info(row['photos']);
    for (var count = 0; count < row['photos'].length; count++) {
        neirong += '<img src="' + '\\' + row['photos'][count] + '" width="100px" height="100px" style="margin-right: 10px;margin-left: 10px;margin-top: 5px;margin-bottom: 5px"/>';
        // console.info(row['photos'][count])
    }
    data.push({
        "biaoqian1": "简介",
        "neirong1": '<textarea  readonly="readonly" style="width: 100%;align-self:right;overflow: auto;word-break: break-all;"  name="' + key + '" rows="4" cols=27>' + row['jianjie'] + '</textarea>'
    });
    data.push({"biaoqian1": "照片:", "neirong1": neirong});
    var cur_table = $detail.html('<table></table>').find('table');
    $(cur_table).bootstrapTable({
        data: data,
        uniqueId: "MENU_ID",
        script: true,
        striped: true,
        columns: [{
            field: 'biaoqian1',
            width: '15%',
            title: ''
        }, {
            field: 'neirong1',
            width: '35%',
            title: ''
        }, {
            field: 'biaoqian2',
            width: '15%',
            title: ''
        }, {
            field: 'neirong2',
            width: '35%',
            title: ''
        }]
    });
    // console.info(index,Math.ceil(index / 2));
    $(cur_table).bootstrapTable('mergeCells', {
        index: Math.ceil(ind / 2) - 1,
        field: "neirong1",
        colspan: 3,
        rowspan: 1
    });
    $(cur_table).bootstrapTable('mergeCells', {index: Math.ceil(ind / 2), field: "neirong1", colspan: 3, rowspan: 1});
    $(cur_table).bootstrapTable('mergeCells', {index: Math.ceil(ind / 2)+1, field: "neirong1", colspan: 3, rowspan: 1});
}
