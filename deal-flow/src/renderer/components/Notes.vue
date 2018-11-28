<template>
    <div class="">
        <div id="editor">
          <p><br></p>
        </div>
    </div>
</template>
<script>
import lib from '../lib'

export default {
    name: 'Notes',
    props: {
        value: null,
        id: null,
        isContact: Boolean,
        isDeal: Boolean,
        isOrganization: Boolean
    },
    data() {
        return {
            quill: null
        }
    },
    mounted() {
        this.quill = new Quill('#editor', {
          theme: 'snow'
      })
      this.quill.root.addEventListener("blur", this.writeData)

    },
    methods: {
        writeData() {
            // console.log('in blur');
            var resource = ''
            if (this.isDeal) resource = '/deals'
            else if (this.isContact) resource = '/contacts'
            else if (this.isOrganization) resource = '/organizations'

            lib.putRequest(resource.concat('/').concat(this.id), { 'notes': JSON.stringify(this.quill.getContents()) }, response => {
                console.log('Successful write');
            })
        }
    },
    watch: {
       myValue: function(newVal, oldVal) {
         this.quill.setContents(JSON.parse(this.myValue))
       }
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
