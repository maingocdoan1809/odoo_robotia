import { useEffect, useState } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";


export class FormReadonlyDefaultController extends FormController {
  static template = `company_management.FormViewReadonlyDefault`;
  setup() {
    this.props.mode = this._recordMode.READONLY;
    super.setup();

    this.formState = useState({
      mode: this.props.mode,
    });

    useEffect(
      () => {
        if (this.model.root.isNew) {
          this.formState.mode = this._recordMode.EDIT
        }
      },
      () => [this.model.root.isNew]
    );
  }
  get _recordMode() {
    return {
      READONLY: "readonly",
      EDIT: "edit",
    };
  }
  toggleMode() {
    const modes = this._recordMode;
    const nextMode =
      this.formState.mode == modes.READONLY ? modes.EDIT : modes.READONLY;
      this.formState.mode = nextMode;
      this.model.root.switchMode(nextMode);
  }

  async onRecordSaved(record, changes) {
    await super.onRecordSaved(record, changes);
    this.toggleMode();
    this.model.notification.add(_t("Record saved successfully"), {
      type: "success",
    });
  }

  async discard() {
    await super.discard();
    this.toggleMode();
  }
  async beforeLeave() {
    // không cho phép tự động lưu khi không còn focus ở form view nữa
    return;
  }
  beforeVisibilityChange() {
    // không cho phép tự động lưu khi không còn focus ở form view nữa
    return;
  }
}

registry.category("views").add("form_readonly_default", {
  ...formView,
  Controller: FormReadonlyDefaultController,
});
