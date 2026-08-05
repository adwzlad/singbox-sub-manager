// =========================
// 保存 ADMIN_KEY
// =========================

function saveKey(){


    const key = document

        .getElementById(

            "adminKey"

        )

        .value;



    localStorage.setItem(

        "adminKey",

        key

    );



    showResult(

        "ADMIN_KEY 已保存"

    );

}









// =========================
// 显示结果
// =========================

function showResult(

    text

){


    document

        .getElementById(

            "result"

        )

        .textContent = text;

}









// =========================
// 页面初始化
// =========================

window.onload = function(){


    const key = localStorage.getItem(

        "adminKey"

    );



    if(key){


        document

            .getElementById(

                "adminKey"

            )

            .value = key;


    }

};
