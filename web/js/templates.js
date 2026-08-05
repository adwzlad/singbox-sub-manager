async function getTemplates(){


    try {


        const data = await apiFetch(

            "/templates"

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
