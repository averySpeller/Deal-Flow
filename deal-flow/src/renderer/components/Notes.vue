<template>
    <div class="">
        <div id="editor">
          <p></p>
        </div>
    </div>
</template>
<script>
export default {
    name: 'FileUploader',
    props: ['value'],
    data() {
        return {
            quill: null
        }
    },
    mounted() {
        this.quill = new Quill('#editor', {
          theme: 'snow'
        })
    },
    methods: {

    }
}
</script>

<style lang="css">

</style>
