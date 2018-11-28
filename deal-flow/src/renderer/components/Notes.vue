<template>
    <div class="">
        <div id="editor">
          <p>{{myValue}}</p>
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

    },
    computed: {
      myValue: {
        get() {
          return this.value;
        },
        set(v) {
          this.$emit('input', v)
        }
      }
}

}
</script>

<style lang="css">

    #editor {
        min-height: 125px;
        max-height: 300px;
    }

</style>
