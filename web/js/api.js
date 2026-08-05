function getAdminKey() {

    return localStorage.getItem(
        "adminKey"
    ) || "";

}





async function apiFetch(

    url,

    options = {}

) {


    options.headers = {

        ...(options.headers || {}),

        "X-Admin-Key": getAdminKey()

    };



    const response = await fetch(

        url,

        options

    );



    const data = await response.json();



    if (!response.ok) {


        throw new Error(

            data.detail ||

            "API error"

        );

    }



    return data;

}
