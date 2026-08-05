async function getHosts(){


    try {


        const data = await apiFetch(

            "/hosts"

        );



        showResult(

            JSON.stringify(

                data,

                null,

                2

            )

        );



    } catch(e) {


        showResult(

            e.message

        );

    }

}
