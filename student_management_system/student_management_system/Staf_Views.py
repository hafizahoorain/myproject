from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_leave
from django.contrib import messages


def HOME(request):
    return render(request,'Staff/staff_home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id = staff_id)
        context ={
            'notification':notification,
        }
    return render(request,'Staff/notification.html',context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')


def STAFF_APPLY_LEAVE(request):
    return render(request,'Staff/apply_leave.html')


def STAFF_APPLY_LEAVE_SAVE(request):
        if request.method == "POST":
            leave_date = request.POST.get('leave_date')
            leave_message = request.POST.get('leave_message')

            # Get the staff object directly using the ForeignKey instead of querying the Staff model
            staff = request.user.staff

            # Use keyword arguments for clarity and to avoid typographical errors
            leave = Staff_leave.objects.create(
                staff_id=staff,
                data=leave_date,
                messsage=leave_message,
            )

            # Instead of using messages.success, we can use Django's built-in messages framework
            messages.success(request, 'Leave Successfully Sent!')

        # Use a more descriptive URL name for redirect
        return redirect('staff_apply_leave')
