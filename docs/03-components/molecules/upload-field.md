# UploadField

> File picker with drag and drop: inline, single image, single video, multiple (row or column).

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-uploader>` |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `inline`, `single-image`, `single-video`, `multiple`, `multiple-vertical` |
| `accept` | string |
| `maxSize` | number |
| `maxFiles` | number |

## States

- default
- filled
- dragging
- uploading
- error

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `upload input` | Inputs | 17 | Langugae: Arabic, English; variant: inline, multiple, multiple vertical, single-image, single-video; state: default, filled; error: false, true |

## Source in the Twilight Storybook today

### `<s-uploader>`

[components-uploader](https://dashboard-ui-components.pages.dev/?path=/docs/components-uploader) · 21 stories · Uploader component allows users to upload files with various layouts and configurations. It supports drag & drop, multiple files, file type restrictions, and preview functionality.

Related elements: `<s-button>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `allowAlt` | boolean | `true` |  | Show the ALT text button/editor under each file preview |
| `autoUpload` | boolean | `false` |  | Enable auto upload to server (deprecated, use server.instantUpload instead) |
| `buttonLabel` | string | `Submit` |  | Button text for file selection |
| `cropShapes` | object | `undefined` |  | Crop shapes for image cropping (e.g., '1:1' or ['1:1', '9:16', '1.91:1']). Restricts cropping to only these shapes. |
| `desc` | string | `""` |  | Description text for the uploader |
| `disabled` | boolean | `false` |  | Disabled state |
| `editable` | boolean | `true` |  | Allow users to edit files |
| `fileSize` | string | `"2MB"` |  | Maximum file size |
| `filesAllowed` | string | `"all"` | `all`, `images`, `videos`, `fonts`, `file` | Allowed file types |
| `has3D` | boolean | `false` |  | Enable 3D image support |
| `hasError` | boolean | `false` |  | Error state |
| `hasPreview` | boolean | `false` |  | Show only preview without uploader area |
| `headers` | object | `undefined` |  | Custom headers for upload (deprecated, use server.headers instead) |
| `hideBrowseButton` | boolean | `false` |  | Hide the built-in browse button and keep only the actions slotted by the consumer (thumbnail layout only) |
| `hideSize` | boolean | `false` |  | Hide file size display |
| `instantEdit` | boolean | `false` |  | Automatically open the image editor after upload completes (thumbnail layout only) |
| `items` | string | `"[]"` |  | Initial files to display |
| `label` | string | `Browse or drag and drop files here` |  | Label text for the uploader |
| `layout` | string | `"drag-drop"` | `inline`, `drag-drop`, `thumbnail` | Uploader layout type |
| `loading` | boolean | `false` |  | Loading state |
| `max` | number | `-1` |  | Maximum number of files (-1 for unlimited) |
| `maxVideos` | number | `undefined` |  | Opt-in cap on video files only (images stay governed by `max`). Unset = no video cap. |
| `method` | object | `null` |  | Upload method for inline layout |
| `multiple` | boolean | `false` |  | Allow multiple file upload |
| `name` | string | `"file"` |  | Name attribute for the input |
| `noBorder` | boolean | `false` |  | Remove border styling |
| `payloadParameters` | object | `null` |  | Additional payload parameters (deprecated, use server.upload.additionalRequestData instead) |
| `placeholder` | string | `Choose a file...` |  | Placeholder text for inline layout |
| `selectable` | boolean | `true` |  | Allow users to select files as primary |
| `server` | object | `undefined` |  | Server configuration object for upload, edit, and remove operations |
| `sortable` | boolean | `true` |  | Enable file sorting |
| `src` | object | `undefined` |  | Upload URL (deprecated, use server.url instead) |
| `verticalThumbnail` | boolean | `false` |  | Use vertical thumbnail layout |

**Events**

| Event | Description |
|---|---|
| `altTextChange` | Event emitted when a file's alt text is changed. Provides the file information. |
| `edit` | Event emitted when a file is edited. Provides the edited file information. |
| `fileUpload` | Event emitted when an item is uploaded (deprecated, use upload instead). |
| `remove` | Event emitted when a file is deleted. Provides the deleted file information. |
| `sort` | Event emitted when a file is reordered. Provides file, newIndex, and oldIndex. |
| `upload` | Event emitted when an item is uploaded. Provides files, file, and error information. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--default), [Inline](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--inline), [Thumbnail](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--thumbnail), [Thumbnail Multiple](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--thumbnail-multiple), [Multiple](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--multiple), [Images Only](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--images-only), [Videos Only](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--videos-only), [Thumbnail Video Player](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--thumbnail-video-player), [With Predefined Items](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--with-predefined-items), [Preview Mode](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--preview-mode), [Non Selectable](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--non-selectable), [Non Editable](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--non-editable), [Non Sortable](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--non-sortable), [Hide File Size](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--hide-file-size), [Alt Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--alt-disabled), [No Border](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--no-border), [Vertical Thumbnail](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--vertical-thumbnail), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--disabled), [With Server Config](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--with-server-config), [With Custom Actions](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--with-custom-actions), [External Editor Trigger](https://dashboard-ui-components.pages.dev/?path=/story/components-uploader--external-editor-trigger)

**Rendered markup (default story)**

```html
<s-uploader name="file" layout="drag-drop" label="Browse or drag and drop files here" placeholder="Choose a file..." button-label="Submit" files-allowed="all" max="-1" file-size="2MB" selectable="" editable="" sortable="" items="[]" class="s-uploader--selectable s-uploader--sortable drag-drop ltr hydrated">
  <p slot="feedback">The suitable image size is 350X263 pixels</p>
</s-uploader>
```


---
_Generated from `catalog/components.json` (id `upload-field`). Edit the catalog, not this file._
