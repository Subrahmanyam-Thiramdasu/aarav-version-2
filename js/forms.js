/**
 * AARAV CLINICS — Appointment Form
 * WhatsApp handoff with validation
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('apptForm');
    if (!form) return;

    const WHATSAPP_NUM = '916302882910';

    function getField(id) {
      return form.querySelector('#' + id);
    }

    function showError(id, message) {
      const field = getField(id);
      if (!field) return;
      field.classList.add('is-error');
      let errEl = field.parentElement.querySelector('.form-field-error');
      if (!errEl) {
        errEl = document.createElement('p');
        errEl.className = 'form-field-error';
        field.parentElement.appendChild(errEl);
      }
      errEl.textContent = message;
    }

    function clearErrors() {
      form.querySelectorAll('.is-error').forEach(function (el) {
        el.classList.remove('is-error');
      });
      form.querySelectorAll('.form-field-error').forEach(function (el) {
        el.remove();
      });
    }

    function validate() {
      clearErrors();
      let valid = true;

      const name = getField('name');
      if (name && !name.value.trim()) {
        showError('name', 'Please enter your name.');
        valid = false;
      }

      const phone = getField('phone');
      if (phone) {
        const phoneVal = phone.value.replace(/\D/g, '');
        if (!phoneVal || phoneVal.length < 10) {
          showError('phone', 'Please enter a valid 10-digit phone number.');
          valid = false;
        }
      }

      return valid;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      if (!validate()) return;

      const name    = (getField('name')    || {}).value || '';
      const phone   = (getField('phone')   || {}).value || '';
      const service = (getField('service') || {}).value || '';
      const message = (getField('message') || {}).value || '';

      const text = encodeURIComponent(
        'Hi Aarav Clinics, I would like to book an appointment.\n\n' +
        'Name: ' + name.trim() + '\n' +
        'Phone: ' + phone.trim() + '\n' +
        'Service: ' + service + '\n' +
        (message.trim() ? 'Message: ' + message.trim() : '')
      );

      const url = 'https://wa.me/' + WHATSAPP_NUM + '?text=' + text;
      window.open(url, '_blank', 'noopener,noreferrer');

      // Show success state
      const successEl = document.getElementById('apptSuccess');
      if (successEl) {
        form.style.display = 'none';
        successEl.classList.add('is-visible');
      }
    });
  });

})();
