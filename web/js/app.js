let adminKey = "";





// =========================
// 保存KEY
// =========================

function saveKey(){


    adminKey = document

        .getElementById(

            "adminKey"

        )

        .value;



    localStorage.setItem(

        "adminKey",

        adminKey

    );



    showResult(

        "ADMIN_KEY 已保存"

    );

}









// =========================
// 请求API
// =========================

async function apiRequest(

    url,

    method="GET"

){


    if(!adminKey){


        adminKey = localStorage.getItem(

            "adminKey"

        );

    }





    let response = await fetch(

        url,

        {

            method:method,


            headers:{


                "X-Admin-Key":

                adminKey

            }

        }

    );



    let data = await response.json();



    showResult(

        JSON.stringify(

            data,

            null,

            2

        )

    );


}









// =========================
// 节点
// =========================

function loadNodes(){


    apiRequest(

        "/nodes"

    );

}









// =========================
// 模板
// =========================

function loadTemplates(){


    apiRequest(

        "/templates"

    );

}









// =========================
// Hosts
// =========================

function loadHosts(){


    apiRequest(

        "/hosts"

    );

}









// =========================
// 显示结果
// =========================

function showResult(

    text

){


    document.getElementById(

        "result"

    ).textContent=text;

}









// =========================
// 初始化
// =========================

window.onload=function(){


    adminKey = localStorage.getItem(

        "adminKey"

    ) || "";

};
